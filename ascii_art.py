"""
ASCII Art and ANSI Color utilities for the BBS
"""

# ANSI Color Codes
class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    
    # Foreground colors
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    
    # Bright foreground colors
    BRIGHT_BLACK = '\033[90m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'
    BRIGHT_CYAN = '\033[96m'
    BRIGHT_WHITE = '\033[97m'
    
    # Background colors
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'


def clear_screen():
    """Return ANSI clear screen sequence"""
    return '\033[2J\033[H'


def colorize(text, color):
    """Wrap text in ANSI color codes"""
    return f"{color}{text}{Colors.RESET}"


LOGO = f"""{Colors.BRIGHT_CYAN}
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║                 {Colors.BRIGHT_YELLOW}█████╗ {Colors.BRIGHT_MAGENTA}██╗{Colors.BRIGHT_CYAN}    {Colors.BRIGHT_GREEN}██████╗ {Colors.BRIGHT_RED}██████╗ {Colors.BRIGHT_BLUE}███████╗{Colors.BRIGHT_CYAN}                    ║
║                {Colors.BRIGHT_YELLOW}██╔══██╗{Colors.BRIGHT_MAGENTA}██║{Colors.BRIGHT_CYAN}    {Colors.BRIGHT_GREEN}██╔══██╗{Colors.BRIGHT_RED}██╔══██╗{Colors.BRIGHT_BLUE}██╔════╝{Colors.BRIGHT_CYAN}                    ║
║                {Colors.BRIGHT_YELLOW}███████║{Colors.BRIGHT_MAGENTA}██║{Colors.BRIGHT_CYAN}    {Colors.BRIGHT_GREEN}██████╔╝{Colors.BRIGHT_RED}██████╔╝{Colors.BRIGHT_BLUE}███████╗{Colors.BRIGHT_CYAN}                    ║
║                {Colors.BRIGHT_YELLOW}██╔══██║{Colors.BRIGHT_MAGENTA}██║{Colors.BRIGHT_CYAN}    {Colors.BRIGHT_GREEN}██╔══██╗{Colors.BRIGHT_RED}██╔══██╗{Colors.BRIGHT_BLUE}╚════██║{Colors.BRIGHT_CYAN}                    ║
║                {Colors.BRIGHT_YELLOW}██║  ██║{Colors.BRIGHT_MAGENTA}██║{Colors.BRIGHT_CYAN}    {Colors.BRIGHT_GREEN}██████╔╝{Colors.BRIGHT_RED}██████╔╝{Colors.BRIGHT_BLUE}███████║{Colors.BRIGHT_CYAN}                    ║
║                {Colors.BRIGHT_YELLOW}╚═╝  ╚═╝{Colors.BRIGHT_MAGENTA}╚═╝{Colors.BRIGHT_CYAN}    {Colors.BRIGHT_GREEN}╚═════╝ {Colors.BRIGHT_RED}╚═════╝ {Colors.BRIGHT_BLUE}╚══════╝{Colors.BRIGHT_CYAN}                    ║
║                                                                           ║         
║              {Colors.BRIGHT_WHITE}AI-Powered Bulletin Board System - Est. 2026{Colors.BRIGHT_CYAN}                 ║
║                  {Colors.BRIGHT_YELLOW}« Where the 90s meet the future »{Colors.BRIGHT_CYAN}                        ║
║                   {Colors.BRIGHT_BLACK}Powered by OpenRouter (Free Tier){Colors.BRIGHT_CYAN}                       ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
{Colors.RESET}"""


MAIN_MENU = f"""{Colors.BRIGHT_CYAN}
╔═══════════════════════════════════════════════════════════════════════════╗
║                            {Colors.BRIGHT_YELLOW}« MAIN MENU »{Colors.BRIGHT_CYAN}                                  ║
╠═══════════════════════════════════════════════════════════════════════════╣
║                                                                           ║
║   {Colors.BRIGHT_GREEN}[1]{Colors.WHITE} Chat with AI                 {Colors.BRIGHT_BLACK}// Talk to the future{Colors.BRIGHT_CYAN}                  ║
║   {Colors.BRIGHT_GREEN}[2]{Colors.WHITE} View Message Boards          {Colors.BRIGHT_BLACK}// Classic BBS vibes{Colors.BRIGHT_CYAN}                   ║
║   {Colors.BRIGHT_GREEN}[3]{Colors.WHITE} ASCII Art Gallery            {Colors.BRIGHT_BLACK}// Retro masterpieces{Colors.BRIGHT_CYAN}                  ║
║   {Colors.BRIGHT_GREEN}[4]{Colors.WHITE} System Information           {Colors.BRIGHT_BLACK}// Stats & info{Colors.BRIGHT_CYAN}                        ║
║   {Colors.BRIGHT_GREEN}[5]{Colors.WHITE} Easter Eggs                  {Colors.BRIGHT_BLACK}// Find the secrets!{Colors.BRIGHT_CYAN}                   ║
║   {Colors.BRIGHT_RED}[Q]{Colors.WHITE} Quit / Logoff                {Colors.BRIGHT_BLACK}// See you later!{Colors.BRIGHT_CYAN}                      ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
{Colors.RESET}"""


CHAT_HEADER = f"""{Colors.BRIGHT_MAGENTA}
╔═══════════════════════════════════════════════════════════════════════════╗
║                         {Colors.BRIGHT_YELLOW}« AI CHAT ROOM »{Colors.BRIGHT_MAGENTA}                                  ║
╠═══════════════════════════════════════════════════════════════════════════╣
║  {Colors.WHITE}You are now connected to AI!{Colors.BRIGHT_MAGENTA}                                             ║   
║  {Colors.BRIGHT_BLACK}Type your message and press ENTER. Type '/exit' to return to menu.{Colors.BRIGHT_MAGENTA}       ║
╚═══════════════════════════════════════════════════════════════════════════╝
{Colors.RESET}"""


COMPUTER_ART = f"""{Colors.BRIGHT_GREEN}
                    _______________
                   |,----------.  |\\
                   ||           |=| |
                   ||          || | |
                   ||       . _o| | |
                   |`-----------' |/
                    ~~~~~~~~~~~~~~~
                 {Colors.BRIGHT_YELLOW}« RETRO COMPUTING »{Colors.RESET}
"""


ROBOT_ART = f"""{Colors.BRIGHT_CYAN}
              .---.
             /     \\
             \\.@-@./
             /`\\_/`\\
            //  _  \\\\
           | \\     )|_
          /`\\_`>  <_/ \\
          \\__/'---'\\__/
       {Colors.BRIGHT_YELLOW}« AI Assistant Ready »{Colors.RESET}
"""


GOODBYE = f"""{Colors.BRIGHT_YELLOW}
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║                     {Colors.BRIGHT_MAGENTA}Thanks for visiting AI BBS!{Colors.BRIGHT_YELLOW}                           ║
║                                                                           ║
║                      {Colors.BRIGHT_CYAN}╔═══════════════════════╗{Colors.BRIGHT_YELLOW}                            ║
║                      {Colors.BRIGHT_CYAN}║     {Colors.BRIGHT_WHITE}See you online!   {Colors.BRIGHT_CYAN}║{Colors.BRIGHT_YELLOW}                            ║
║                      {Colors.BRIGHT_CYAN}╚═══════════════════════╝{Colors.BRIGHT_YELLOW}                            ║
║                                                                           ║
║                 {Colors.BRIGHT_GREEN}Connection will close in 3 seconds...{Colors.BRIGHT_YELLOW}                     ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
{Colors.RESET}"""


LOADING_FRAMES = [
    f"{Colors.BRIGHT_CYAN}[{Colors.BRIGHT_YELLOW}■{Colors.BRIGHT_BLACK}□□□□□□□□□{Colors.BRIGHT_CYAN}]{Colors.RESET}",
    f"{Colors.BRIGHT_CYAN}[{Colors.BRIGHT_YELLOW}■■{Colors.BRIGHT_BLACK}□□□□□□□□{Colors.BRIGHT_CYAN}]{Colors.RESET}",
    f"{Colors.BRIGHT_CYAN}[{Colors.BRIGHT_YELLOW}■■■{Colors.BRIGHT_BLACK}□□□□□□□{Colors.BRIGHT_CYAN}]{Colors.RESET}",
    f"{Colors.BRIGHT_CYAN}[{Colors.BRIGHT_YELLOW}■■■■{Colors.BRIGHT_BLACK}□□□□□□{Colors.BRIGHT_CYAN}]{Colors.RESET}",
    f"{Colors.BRIGHT_CYAN}[{Colors.BRIGHT_YELLOW}■■■■■{Colors.BRIGHT_BLACK}□□□□□{Colors.BRIGHT_CYAN}]{Colors.RESET}",
    f"{Colors.BRIGHT_CYAN}[{Colors.BRIGHT_YELLOW}■■■■■■{Colors.BRIGHT_BLACK}□□□□{Colors.BRIGHT_CYAN}]{Colors.RESET}",
    f"{Colors.BRIGHT_CYAN}[{Colors.BRIGHT_YELLOW}■■■■■■■{Colors.BRIGHT_BLACK}□□□{Colors.BRIGHT_CYAN}]{Colors.RESET}",
    f"{Colors.BRIGHT_CYAN}[{Colors.BRIGHT_YELLOW}■■■■■■■■{Colors.BRIGHT_BLACK}□□{Colors.BRIGHT_CYAN}]{Colors.RESET}",
    f"{Colors.BRIGHT_CYAN}[{Colors.BRIGHT_YELLOW}■■■■■■■■■{Colors.BRIGHT_BLACK}□{Colors.BRIGHT_CYAN}]{Colors.RESET}",
    f"{Colors.BRIGHT_CYAN}[{Colors.BRIGHT_YELLOW}■■■■■■■■■■{Colors.BRIGHT_CYAN}]{Colors.RESET}",
]


EASTER_EGG_MATRIX = f"""{Colors.BRIGHT_GREEN}
 ╔═══════════════════════════════════════════════════════════════╗
 ║  01001000 01100101 01101100 01101100 01101111 00100001        ║
 ║  {Colors.BRIGHT_WHITE}You found the Matrix Easter Egg!{Colors.BRIGHT_GREEN}                             ║
 ║  {Colors.BRIGHT_CYAN}« There is no spoon »{Colors.BRIGHT_GREEN}                                        ║
 ╚═══════════════════════════════════════════════════════════════╝
{Colors.RESET}"""


def get_typing_effect(text, color=Colors.WHITE):
    """Returns text with color for typing effect"""
    return f"{color}{text}{Colors.RESET}"
