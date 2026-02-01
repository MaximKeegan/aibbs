"""
Main BBS Server - Telnet-based Bulletin Board System
"""
import socket
import socketserver
import paramiko
import threading
import time
import os
from datetime import datetime
from ascii_art import *
from ai_client import AIClient


class BBSHandler(socketserver.BaseRequestHandler):
    """Handler for individual BBS connections"""
    
    def __init__(self, *args, **kwargs):
        self.username = "Guest"
        self.ai_client = None
        super().__init__(*args, **kwargs)
    
    def send(self, message):
        """Send message to client with UTF-8 encoding"""
        try:
            # Ensure proper line endings (CRLF) for both Telnet and SSH/PTY
            # This fixes the "staircase effect" where ASCII art falls apart
            if isinstance(message, str):
                message = message.replace('\r\n', '\n').replace('\n', '\r\n')
            
            # Ensure proper UTF-8 encoding for Cyrillic and other Unicode characters
            self.request.sendall(message.encode('utf-8', errors='replace'))
        except Exception as e:
            print(f"Error sending message: {e}")
    
    def negotiate_telnet(self):
        """Send Telnet negotiation codes to force character mode"""
        if getattr(self.request, 'is_ssh', False):
            return
            
        # IAC WILL ECHO (255 251 1)
        # IAC WILL SUPPRESS-GO-AHEAD (255 251 3)
        # IAC WONT LINEMODE (255 252 34)
        # IAC DO BINARY (255 253 0) - Please send 8-bit data
        # IAC WILL BINARY (255 251 0) - I will send 8-bit data
        msg = b'\xff\xfb\x01\xff\xfb\x03\xff\xfc\x22\xff\xfd\x00\xff\xfb\x00'
        try:
            self.request.sendall(msg)
        except Exception as e:
            print(f"Telnet negotiation error: {e}")

    def receive(self, prompt=""):
        """Receive input from client with UTF-8 decoding and line editing"""
        try:
            if prompt:
                self.send(prompt)

            is_ssh = getattr(self.request, 'is_ssh', False)
            buffer = []
            byte_buffer = b""  # Buffer for incomplete UTF-8 sequences
            
            while True:
                # Read one byte at a time
                try:
                    chunk = self.request.recv(1)
                    if not chunk:
                        break
                    
                    # Handle Telnet Commands (IAC)
                    if not is_ssh and chunk == b'\xff':
                        # Read command
                        cmd = self.request.recv(1)
                        if not cmd: break
                        
                        # Handle option negotiation (3-byte commands)
                        # WILL, WONT, DO, DONT
                        if cmd in [b'\xfb', b'\xfc', b'\xfd', b'\xfe']:
                            opt = self.request.recv(1)
                            continue # Ignore negotiation
                        
                        # Handle escaped 255 (double IAC)
                        if cmd == b'\xff':
                            pass # allow generic processing as 0xFF
                        else:
                            continue # Ignore other commands
                
                    if not is_ssh and chunk == b'\xff' and cmd == b'\xff':
                        # Valid 0xFF data case
                        byte_buffer += b'\xff'
                    elif not is_ssh and chunk == b'\xff':
                        continue # Should have been handled above, but safety
                    else:
                        # Normal data
                        byte_buffer += chunk
                    
                    # Try to decode the accumulated bytes
                    try:
                        char = byte_buffer.decode('utf-8')
                        # If successful, clear the byte buffer
                        byte_buffer = b""
                    except UnicodeDecodeError:
                        # Incomplete multibyte sequence, wait for more bytes
                        if len(byte_buffer) > 4: # Safety valve for garbage
                            byte_buffer = b""
                        continue
                        
                except Exception:
                    break

                # Handle Enter (CR or LF)
                if char == '\r' or char == '\n':
                    self.send('\r\n')  # Echo newline to user
                    break
                
                # Handle Backspace (ASCII 127 or 8)
                if char == '\x7f' or char == '\x08':
                    if buffer:
                        buffer.pop()
                        self.send('\x08 \x08')  # Erase character on screen
                    continue
                
                # Handle regular characters
                if char.isprintable():
                    buffer.append(char)
                    self.send(char)  # Echo character back to user
            
            return "".join(buffer)

        except Exception as e:
            print(f"Error receiving data: {e}")
            return ""
    
    def show_loading(self, message="Loading"):
        """Show animated loading bar"""
        self.send(f"\n{Colors.BRIGHT_CYAN}{message}... {Colors.RESET}")
        for frame in LOADING_FRAMES:
            self.send(f"\r{message}... {frame}")
            time.sleep(0.1)
        self.send("\n")
    
    def typing_effect(self, text, delay=0.03):
        """Display text with typing effect"""
        for char in text:
            self.send(char)
            time.sleep(delay)
    
    def show_welcome(self):
        """Display welcome screen"""
        self.send(clear_screen())
        self.send(LOGO)
        self.send(f"\n{Colors.BRIGHT_CYAN}╔═══════════════════════════════════════════════════════════════════════════╗{Colors.RESET}\n")
        self.send(f"{Colors.BRIGHT_CYAN}║{Colors.RESET}  {Colors.BRIGHT_WHITE}Welcome to AI BBS!{Colors.RESET}                                                       {Colors.BRIGHT_CYAN}║{Colors.RESET}\n")
        self.send(f"{Colors.BRIGHT_CYAN}╚═══════════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n\n")
        
        username = self.receive(f"{Colors.BRIGHT_YELLOW}Enter your handle: {Colors.RESET}")
        if username:
            self.username = username[:20]  # Limit username length
        
        self.send(f"\n{Colors.BRIGHT_GREEN}Welcome aboard, {self.username}!{Colors.RESET}\n")
        time.sleep(1)
    
    def show_main_menu(self):
        """Display main menu"""
        self.send(clear_screen())
        self.send(LOGO)
        self.send(MAIN_MENU)
        self.send(f"\n{Colors.BRIGHT_YELLOW}Logged in as: {Colors.BRIGHT_WHITE}{self.username}{Colors.RESET}\n")
        self.send(f"{Colors.BRIGHT_BLACK}Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Colors.RESET}\n\n")
    
    def chat_with_ai(self):
        """AI Chat interface"""
        self.send(clear_screen())
        self.send(CHAT_HEADER)
        self.send(ROBOT_ART)
        self.send("\n")
        
        # Initialize AI client if not already done
        if not self.ai_client:
            try:
                self.show_loading("Connecting to AI")
                self.ai_client = AIClient()
                model_name = self.ai_client.get_model_name()
                self.send(f"{Colors.BRIGHT_GREEN}✓ Connected successfully!{Colors.RESET}\n")
                self.send(f"{Colors.BRIGHT_BLACK}Using model: {model_name}{Colors.RESET}\n\n")
            except Exception as e:
                self.send(f"{Colors.BRIGHT_RED}✗ Error: {str(e)}{Colors.RESET}\n")
                self.send(f"{Colors.BRIGHT_YELLOW}Make sure OPENROUTER_API_KEY is set in .env file{Colors.RESET}\n\n")
                self.receive("Press ENTER to continue...")
                return
        
        while True:
            user_input = self.receive(f"{Colors.BRIGHT_CYAN}{self.username}>{Colors.RESET} ")
            
            if not user_input:
                continue
            
            if user_input.lower() in ['/exit', '/quit', '/back']:
                break
            
            if user_input.lower() == '/reset':
                self.ai_client.reset_conversation()
                self.send(f"{Colors.BRIGHT_YELLOW}Conversation reset!{Colors.RESET}\n\n")
                continue
            
            if user_input.lower() == '/help':
                self.send(f"\n{Colors.BRIGHT_YELLOW}Commands:{Colors.RESET}\n")
                self.send(f"  {Colors.BRIGHT_GREEN}/exit{Colors.RESET}  - Return to main menu\n")
                self.send(f"  {Colors.BRIGHT_GREEN}/reset{Colors.RESET} - Clear conversation history\n")
                self.send(f"  {Colors.BRIGHT_GREEN}/help{Colors.RESET}  - Show this help\n\n")
                continue
            
            # Show thinking animation
            self.send(f"{Colors.BRIGHT_MAGENTA}AI is thinking{Colors.RESET}")
            for _ in range(3):
                self.send(".")
                time.sleep(0.3)
            self.send("\n\n")
            
            # Get AI response
            response = self.ai_client.chat(user_input)
            
            # Display response with typing effect
            self.send(f"{Colors.BRIGHT_MAGENTA}AI>{Colors.RESET} ")
            self.typing_effect(response, delay=0.01)
            self.send("\n\n")
    
    def show_message_boards(self):
        """Display message boards (placeholder)"""
        self.send(clear_screen())
        self.send(f"{Colors.BRIGHT_CYAN}╔═══════════════════════════════════════════════════════════════════════════╗{Colors.RESET}\n")
        self.send(f"{Colors.BRIGHT_CYAN}║{Colors.RESET}                        {Colors.BRIGHT_YELLOW}« MESSAGE BOARDS »{Colors.RESET}                                 {Colors.BRIGHT_CYAN}║{Colors.RESET}\n")
        self.send(f"{Colors.BRIGHT_CYAN}╚═══════════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n\n")
        
        boards = [
            ("General Discussion", "42", "Talk about anything!"),
            ("Tech Talk", "128", "Computers, coding, and more"),
            ("AI & Future", "89", "Discuss AI and the future"),
            ("Retro Computing", "156", "Old school tech nostalgia"),
            ("Off Topic", "73", "Random stuff goes here"),
        ]
        
        for i, (name, posts, desc) in enumerate(boards, 1):
            self.send(f"{Colors.BRIGHT_GREEN}[{i}]{Colors.RESET} {Colors.BRIGHT_WHITE}{name:<25}{Colors.RESET} ")
            self.send(f"{Colors.BRIGHT_YELLOW}({posts} posts){Colors.RESET} - {Colors.BRIGHT_BLACK}{desc}{Colors.RESET}\n")
        
        self.send(f"\n{Colors.BRIGHT_BLACK}[This is a demo - message boards coming soon!]{Colors.RESET}\n\n")
        self.receive("Press ENTER to continue...")
    
    def show_ascii_gallery(self):
        """Display ASCII art gallery"""
        self.send(clear_screen())
        self.send(f"{Colors.BRIGHT_CYAN}╔═══════════════════════════════════════════════════════════════════════════╗{Colors.RESET}\n")
        self.send(f"{Colors.BRIGHT_CYAN}║{Colors.RESET}                      {Colors.BRIGHT_YELLOW}« ASCII ART GALLERY »{Colors.RESET}                                {Colors.BRIGHT_CYAN}║{Colors.RESET}\n")
        self.send(f"{Colors.BRIGHT_CYAN}╚═══════════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n\n")
        
        arts = [COMPUTER_ART, ROBOT_ART]
        
        for art in arts:
            self.send(art)
            self.send("\n")
            time.sleep(1)
        
        self.receive("\nPress ENTER to continue...")
    
    def show_system_info(self):
        """Display system information"""
        self.send(clear_screen())
        self.send(f"{Colors.BRIGHT_CYAN}╔═══════════════════════════════════════════════════════════════════════════╗{Colors.RESET}\n")
        self.send(f"{Colors.BRIGHT_CYAN}║{Colors.RESET}                     {Colors.BRIGHT_YELLOW}« SYSTEM INFORMATION »{Colors.RESET}                                {Colors.BRIGHT_CYAN}║{Colors.RESET}\n")
        self.send(f"{Colors.BRIGHT_CYAN}╚═══════════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n\n")
        
        # Get AI model info if available
        ai_model = "Not connected"
        if self.ai_client:
            ai_model = self.ai_client.get_model_name()
        
        info = [
            ("BBS Name", "AI BBS (Retro Edition)"),
            ("Version", "1.0.0"),
            ("Established", "2026"),
            ("AI Provider", "OpenRouter (Free Tier)"),
            ("AI Model", ai_model),
            ("Your Handle", self.username),
            ("Connection", f"{self.client_address[0]}:{self.client_address[1]}"),
            ("Server Time", datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
            ("Uptime", "Running in Docker"),
        ]
        
        for key, value in info:
            self.send(f"{Colors.BRIGHT_GREEN}{key:.<30}{Colors.RESET} {Colors.BRIGHT_WHITE}{value}{Colors.RESET}\n")
        
        self.send(f"\n{Colors.BRIGHT_YELLOW}« Powered by Python & OpenRouter AI »{Colors.RESET}\n\n")
        self.receive("Press ENTER to continue...")
    
    def show_easter_eggs(self):
        """Display easter eggs menu"""
        self.send(clear_screen())
        self.send(f"{Colors.BRIGHT_CYAN}╔═══════════════════════════════════════════════════════════════════════════╗{Colors.RESET}\n")
        self.send(f"{Colors.BRIGHT_CYAN}║{Colors.RESET}                        {Colors.BRIGHT_YELLOW}« EASTER EGGS »{Colors.RESET}                                    {Colors.BRIGHT_CYAN}║{Colors.RESET}\n")
        self.send(f"{Colors.BRIGHT_CYAN}╚═══════════════════════════════════════════════════════════════════════════╝{Colors.RESET}\n\n")
        
        self.send(EASTER_EGG_MATRIX)
        self.send("\n")
        
        # Fun retro messages
        messages = [
            "🎮 Konami Code: ↑↑↓↓←→←→BA",
            "💾 Remember to save your work on floppy disks!",
            "📞 Dial-up modem sounds: *SCREEEEECH* *BEEEP* *STATIC*",
            "🌐 You've got mail!",
            "⌨️  Press F to pay respects",
        ]
        
        for msg in messages:
            self.send(f"{Colors.BRIGHT_YELLOW}★{Colors.RESET} {msg}\n")
            time.sleep(0.5)
        
        self.send(f"\n{Colors.BRIGHT_BLACK}[More secrets hidden throughout the BBS...]{Colors.RESET}\n\n")
        self.receive("Press ENTER to continue...")
    
    def handle(self):
        """Main handler for BBS connection"""
        try:
            # Negotiate Telnet options (force character mode)
            self.negotiate_telnet()
            
            # Show welcome screen
            self.show_welcome()
            
            # Main menu loop
            while True:
                self.show_main_menu()
                choice = self.receive(f"{Colors.BRIGHT_YELLOW}Enter your choice: {Colors.RESET}")
                
                if choice == '1':
                    self.chat_with_ai()
                elif choice == '2':
                    self.show_message_boards()
                elif choice == '3':
                    self.show_ascii_gallery()
                elif choice == '4':
                    self.show_system_info()
                elif choice == '5':
                    self.show_easter_eggs()
                elif choice.lower() in ['q', 'quit', 'exit']:
                    break
                else:
                    self.send(f"\n{Colors.BRIGHT_RED}Invalid choice! Please try again.{Colors.RESET}\n")
                    time.sleep(1)
            
            # Show goodbye screen
            self.send(clear_screen())
            self.send(GOODBYE)
            time.sleep(3)
            
        except Exception as e:
            print(f"Error in handler: {e}")
        finally:
            self.request.close()


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """Threaded TCP server for handling multiple connections"""
    allow_reuse_address = True


class ParamikoSocketAdapter:
    """Adapts a Paramiko channel to look like a socket for BBSHandler"""
    def __init__(self, channel):
        self.channel = channel
        self.is_ssh = True

    def sendall(self, data):
        sent = 0
        while sent < len(data):
            n = self.channel.send(data[sent:])
            if n == 0:
                raise RuntimeError("Channel closed")
            sent += n

    def recv(self, n):
        return self.channel.recv(n)

    def close(self):
        self.channel.close()


class BBS_SSHInterface(paramiko.ServerInterface):
    """Handle SSH authentication and channel requests"""
    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        return paramiko.AUTH_SUCCESSFUL

    def check_auth_none(self, username):
        return paramiko.AUTH_SUCCESSFUL
    
    def get_allowed_auths(self, username):
        return 'none,password'
    
    def check_channel_shell_request(self, channel):
        return True

    def check_channel_pty_request(self, channel, term, width, height, pixelwidth, pixelheight, modes):
        return True


def handle_ssh_connection(client_sock, host_key):
    """Handle a single SSH connection"""
    transport = paramiko.Transport(client_sock)
    try:
        transport.add_server_key(host_key)
        server = BBS_SSHInterface()
        try:
            transport.start_server(server=server)
        except paramiko.SSHException:
            return

        # Wait for a channel
        channel = transport.accept(20)
        if channel is None:
            return
        
        # Simple wait for the client to be ready (shell/pty negotiation handled by callbacks)
        # BBSHandler expects a synchronous socket-like object
        adapter = ParamikoSocketAdapter(channel)
        client_addr = client_sock.getpeername()
        
        try:
            # BBSHandler handles the entire session
            BBSHandler(adapter, client_addr, None)
        except Exception as e:
            print(f"SSH Handler Error: {e}")
        finally:
            adapter.close()
            
    except Exception as e:
        print(f"SSH Transport Error: {e}")
    finally:
        transport.close()
        client_sock.close()


def run_ssh_server(port, host_key_path='data/ssh_host_key'):
    """Main loop for SSH server"""
    # Load or generate host key
    # Ensure data directory exists
    os.makedirs(os.path.dirname(host_key_path), exist_ok=True)
    
    if not os.path.exists(host_key_path):
        print(f"Generating SSH host key at {host_key_path}...")
        key = paramiko.RSAKey.generate(2048)
        key.write_private_key_file(host_key_path)
    
    host_key = paramiko.RSAKey(filename=host_key_path)
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('0.0.0.0', port))
    sock.listen(100)
    
    print(f"SSH Server listening on 0.0.0.0:{port}")
    
    while True:
        try:
            client, addr = sock.accept()
            t = threading.Thread(target=handle_ssh_connection, args=(client, host_key))
            t.daemon = True
            t.start()
        except Exception as e:
            print(f"Error accepting SSH connection: {e}")


def main():
    """Main server function"""
    HOST = '0.0.0.0'
    HOST = '0.0.0.0'
    PORT = int(os.getenv('BBS_PORT', 2323))
    SSH_PORT = int(os.getenv('SSH_PORT', 2222))
    
    print(f"""
╔═══════════════════════════════════════════════════════════════════════════╗
║                     AI BBS Server Starting...                             ║
║                     Powered by OpenRouter (Free Tier)                     ║
╚═══════════════════════════════════════════════════════════════════════════╝
    """)
    
    print(f"Server listening on {HOST}:{PORT}")
    print(f"Connect via telnet: telnet localhost {PORT}")
    print(f"Connect via ssh:    ssh -p {SSH_PORT} guest@localhost")
    print(f"\nPress Ctrl+C to stop the server\n")
    
    # Start SSH Server in background thread
    ssh_thread = threading.Thread(target=run_ssh_server, args=(SSH_PORT,))
    ssh_thread.daemon = True
    ssh_thread.start()
    
    server = ThreadedTCPServer((HOST, PORT), BBSHandler)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n\nShutting down server...")
        server.shutdown()
        server.server_close()
        print("Server stopped.")


if __name__ == "__main__":
    main()
