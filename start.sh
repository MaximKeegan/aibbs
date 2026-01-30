#!/bin/bash

echo "╔═══════════════════════════════════════════════════════════════════════════╗"
echo "║                     DeepSeek BBS - Quick Start                            ║"
echo "╚═══════════════════════════════════════════════════════════════════════════╝"
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "⚠️  .env file not found!"
    echo "Creating .env from .env.example..."
    cp .env.example .env
    echo ""
    echo "📝 Please edit .env and add your DeepSeek API key:"
    echo "   DEEPSEEK_API_KEY=your_actual_api_key_here"
    echo ""
    echo "Get your API key at: https://platform.deepseek.com/"
    echo ""
    read -p "Press ENTER after you've added your API key..."
fi

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "❌ Docker is not running. Please start Docker and try again."
    exit 1
fi

echo "🐳 Building and starting DeepSeek BBS..."
echo ""

docker-compose up --build -d

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ DeepSeek BBS is now running!"
    echo ""
    echo "╔═══════════════════════════════════════════════════════════════════════════╗"
    echo "║                        How to Connect                                     ║"
    echo "╠═══════════════════════════════════════════════════════════════════════════╣"
    echo "║                                                                           ║"
    echo "║  Open a new terminal and run:                                            ║"
    echo "║                                                                           ║"
    echo "║    telnet localhost 2323                                                 ║"
    echo "║                                                                           ║"
    echo "║  Or if telnet is not available:                                          ║"
    echo "║                                                                           ║"
    echo "║    nc localhost 2323                                                     ║"
    echo "║                                                                           ║"
    echo "╚═══════════════════════════════════════════════════════════════════════════╝"
    echo ""
    echo "📋 Useful commands:"
    echo "   docker-compose logs -f    # View logs"
    echo "   docker-compose down       # Stop the BBS"
    echo "   docker-compose restart    # Restart the BBS"
    echo ""
else
    echo "❌ Failed to start DeepSeek BBS"
    echo "Check the error messages above for details."
    exit 1
fi
