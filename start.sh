#!/bin/bash

# Fix for "UnicodeEncodeError: 'ascii' codec can't encode characters"
# on older servers with generic locales
export LANG=en_US.UTF-8
export LC_ALL=en_US.UTF-8
export PYTHONIOENCODING=utf-8

echo "╔═══════════════════════════════════════════════════════════════════════════╗"
echo "║                     AI BBS - Server Launcher                              ║"
echo "╚═══════════════════════════════════════════════════════════════════════════╝"
echo ""

# Check if .env exists
if [ ! -f .env ]; then
    echo "⚠️  .env file not found!"
    if [ -f .env.example ]; then
        echo "Creating .env from .env.example..."
        cp .env.example .env
        echo "📝 Please edit .env and add your OpenRouter API key"
    else
        echo "❌ .env.example also not found. Please create .env manually."
        exit 1
    fi
fi

echo "🐳 Building and starting AI BBS..."
echo "   (Using UTF-8 encoding fix for older docker-compose)"
echo ""

# Run docker-compose with force-recreate to ensure updates are applied
# Using the python encoding fix inline as well just in case
PYTHONIOENCODING=utf-8 docker-compose up --build -d

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ AI BBS is running!"
    echo "   Connect using: telnet localhost 2323"
    echo "   Connect using: ssh -p 2222 guest@localhost"
    echo ""
    echo "   Logs: docker-compose logs -f"
    echo "   Stop: docker-compose down"
else
    echo ""
    echo "❌ Start failed. Showing logs..."
    docker-compose logs --tail=20
fi
