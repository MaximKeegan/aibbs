# AI BBS 🖥️

A beautiful retro Bulletin Board System (BBS) with AI-powered chat using **OpenRouter's free tier**! Experience the nostalgia of 90s BBS culture with modern AI technology - completely free!

## Features ✨

- 🎨 **Beautiful ASCII Art** - Stunning retro graphics and ANSI colors
- 🤖 **AI Chat** - Talk to AI in a classic BBS interface (using free models!)
- 🌍 **Multilingual Support** - Full UTF-8 support including Cyrillic (Russian), Chinese, and more
- 📡 **Telnet Access** - Connect via telnet like the good old days
- 🎭 **Interactive Menus** - Navigate through classic BBS-style menus
- 🎮 **Easter Eggs** - Hidden surprises throughout the system
- 🐳 **Docker Ready** - Easy deployment with Docker Compose
- 🌈 **Retro Aesthetics** - ANSI colors, typing effects, and loading animations
- 💰 **100% Free** - Uses OpenRouter's free tier models (no credit card required!)

## Quick Start 🚀

### Prerequisites

- Docker and Docker Compose installed
- OpenRouter API key ([Get one FREE here](https://openrouter.ai/keys)) - No credit card required!

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd aibbs
   ```

2. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your OpenRouter API key:
   ```
   OPENROUTER_API_KEY=your_actual_api_key_here
   AI_MODEL=google/gemma-2-9b-it:free
   ```
   
   **Get your FREE API key:**
   1. Go to [https://openrouter.ai/keys](https://openrouter.ai/keys)
   2. Sign up (no credit card required!)
   3. Create a new API key
   4. Copy it to your `.env` file

3. **Build and run with Docker Compose**
   ```bash
   docker-compose up --build
   ```

4. **Connect to the BBS**
   
   Open a new terminal and connect via telnet:
   ```bash
   telnet localhost 2323
   ```

   Or use netcat if telnet is not available:
   ```bash
   nc localhost 2323
   ```

## Usage 📖

Once connected, you'll see the beautiful AI BBS welcome screen!

### Main Menu Options

1. **Chat with AI** - Have a conversation with AI
2. **View Message Boards** - Classic BBS message boards (demo)
3. **ASCII Art Gallery** - View retro ASCII artwork
4. **System Information** - See BBS stats and info
5. **Easter Eggs** - Discover hidden surprises
6. **Quit** - Disconnect from the BBS

### Chat Commands

While in the AI chat room:
- `/exit` - Return to main menu
- `/reset` - Clear conversation history
- `/help` - Show available commands

## Project Structure 📁

```
aibbs/
├── bbs_server.py          # Main BBS server
├── ai_client.py           # OpenRouter AI integration
├── ascii_art.py           # ASCII art and ANSI colors
├── test_encoding.py       # UTF-8 encoding test
├── docker-compose.yml     # Docker Compose configuration
├── Dockerfile             # Docker image definition
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variables template
├── MULTILINGUAL.md        # Multilingual support guide
└── README.md              # This file
```

## Configuration ⚙️

### Environment Variables

- `OPENROUTER_API_KEY` - Your OpenRouter API key (required, FREE!)
- `AI_MODEL` - AI model to use (default: google/gemma-2-9b-it:free)
- `BBS_PORT` - Port for telnet server (default: 2323)

**Available Free Models:**
- `google/gemma-2-9b-it:free` (default, recommended)
- `meta-llama/llama-3.2-3b-instruct:free`
- `microsoft/phi-3-mini-128k-instruct:free`
- See more at [OpenRouter Models](https://openrouter.ai/models?order=newest&supported_parameters=tools&max_price=0)

### Customization

You can customize the BBS by editing:
- `ascii_art.py` - Add your own ASCII art and color schemes
- `bbs_server.py` - Modify menus and add new features
- `ai_client.py` - Adjust AI behavior, prompts, or change models

## Development 🛠️

### Running Locally (without Docker)

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up `.env` file with your API key

3. Run the server:
   ```bash
   python bbs_server.py
   ```

4. Connect via telnet:
   ```bash
   telnet localhost 2323
   ```

### Docker Commands

```bash
# Build and start
docker-compose up --build

# Run in background
docker-compose up -d

# View logs
docker-compose logs -f

# Stop the server
docker-compose down

# Rebuild after changes
docker-compose up --build --force-recreate
```

## Features in Detail 🎯

### ASCII Art & ANSI Colors
- Full ANSI color support with 16 colors
- Custom ASCII art for logos and decorations
- Animated loading bars and typing effects
- Retro computer and robot ASCII art

### AI Integration
- Powered by OpenRouter's free tier
- Multiple free models available
- Maintains conversation history
- Retro-themed AI personality
- Concise responses optimized for terminal display
- Multilingual support (English, Russian, Chinese, etc.)

### Telnet Server
- Multi-threaded for multiple simultaneous connections
- Handles user input and output gracefully
- Clean connection handling and error recovery

## Troubleshooting 🔧

### Can't connect via telnet?
- Make sure the Docker container is running: `docker-compose ps`
- Check if port 2323 is available: `lsof -i :2323`
- Try using `nc localhost 2323` instead of telnet

### API errors?
- Verify your OpenRouter API key is correct in `.env`
- Check your API quota at https://openrouter.ai/
- Make sure you're using a free model (models ending in `:free`)
- Look at Docker logs: `docker-compose logs`

### No colors showing?
- Make sure your terminal supports ANSI colors
- Try a different terminal emulator (iTerm2, Windows Terminal, etc.)

### Cyrillic or Unicode characters corrupted?
- Make sure your terminal is set to UTF-8 encoding
- On macOS/Linux: Your terminal should use UTF-8 by default
- On Windows: Use Windows Terminal or PuTTY with UTF-8 encoding enabled
- Test encoding with: `python test_encoding.py`
- If using PuTTY: Go to Window → Translation → Remote character set → UTF-8

## Contributing 🤝

Feel free to contribute! Some ideas:
- Add more ASCII art
- Implement actual message boards with persistence
- Add user authentication
- Create more interactive features
- Add games or utilities

## License 📄

MIT License - Feel free to use and modify!

## Credits 🙏

- Built with Python and love for retro computing
- Powered by [OpenRouter](https://openrouter.ai/) - Free AI API aggregator
- Inspired by classic BBS systems of the 1990s
- Free AI models from Google, Meta, Microsoft, and others

## Screenshots 📸

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║      █████╗ ██╗    ██████╗ ██████╗ ███████╗                              ║
║     ██╔══██╗██║    ██╔══██╗██╔══██╗██╔════╝                              ║
║     ███████║██║    ██████╔╝██████╔╝███████╗                              ║
║     ██╔══██║██║    ██╔══██╗██╔══██╗╚════██║                              ║
║     ██║  ██║██║    ██████╔╝██████╔╝███████║                              ║
║     ╚═╝  ╚═╝╚═╝    ╚═════╝ ╚═════╝ ╚══════╝                              ║
║                                                                           ║
║              AI-Powered Bulletin Board System - Est. 2026                ║
║                  « Where the 90s meet the future »                       ║
║                   Powered by OpenRouter (Free Tier)                      ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

---

**Enjoy your journey back to the BBS era! 🚀**
