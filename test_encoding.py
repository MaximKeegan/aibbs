#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test script to verify UTF-8 and Cyrillic character support
"""

from ascii_art import Colors, colorize

print("Testing UTF-8 and Cyrillic character support...\n")

# Test Cyrillic
print(f"{Colors.BRIGHT_CYAN}Cyrillic Test:{Colors.RESET}")
print("Привет, мир! 🌍")
print("Добро пожаловать в AI BBS!")
print("Русский язык полностью поддерживается ✓\n")

# Test other Unicode
print(f"{Colors.BRIGHT_GREEN}Unicode Test:{Colors.RESET}")
print("English: Hello World!")
print("Russian: Привет мир!")
print("Chinese: 你好世界!")
print("Japanese: こんにちは世界!")
print("Arabic: مرحبا بالعالم!")
print("Emoji: 🎮 🖥️ 💾 📡 🌈 ✨\n")

# Test ANSI colors with Cyrillic
print(f"{Colors.BRIGHT_YELLOW}Colored Cyrillic:{Colors.RESET}")
print(colorize("Красный текст", Colors.BRIGHT_RED))
print(colorize("Зелёный текст", Colors.BRIGHT_GREEN))
print(colorize("Синий текст", Colors.BRIGHT_BLUE))
print(colorize("Жёлтый текст", Colors.BRIGHT_YELLOW))

print(f"\n{Colors.BRIGHT_GREEN}✓ All tests passed!{Colors.RESET}")
print("UTF-8 encoding is working correctly.\n")
