# Multilingual Support / Многоязычная поддержка

## English

AI BBS fully supports UTF-8 encoding, which means you can:
- Chat with AI in any language (English, Russian, Chinese, Japanese, Arabic, etc.)
- Use Cyrillic characters in usernames and messages
- See emoji and special Unicode characters correctly

### Terminal Setup
Make sure your terminal is configured for UTF-8:
- **macOS Terminal/iTerm2**: UTF-8 by default ✓
- **Linux**: Usually UTF-8 by default ✓
- **Windows**: Use Windows Terminal or configure PuTTY for UTF-8

---

## Русский (Russian)

AI BBS полностью поддерживает кодировку UTF-8, что означает:
- Вы можете общаться с AI на любом языке (английский, русский, китайский, японский, арабский и т.д.)
- Использовать кириллицу в именах пользователей и сообщениях
- Корректно видеть эмодзи и специальные Unicode символы

### Настройка терминала
Убедитесь, что ваш терминал настроен на UTF-8:
- **macOS Terminal/iTerm2**: UTF-8 по умолчанию ✓
- **Linux**: Обычно UTF-8 по умолчанию ✓
- **Windows**: Используйте Windows Terminal или настройте PuTTY на UTF-8

### Настройка PuTTY (Windows)
1. Откройте настройки PuTTY
2. Перейдите в Window → Translation
3. Установите "Remote character set" в "UTF-8"
4. Сохраните настройки

---

## Testing / Тестирование

Run the test script to verify encoding:
```bash
python test_encoding.py
```

Запустите тестовый скрипт для проверки кодировки:
```bash
python test_encoding.py
```

---

## Example Chat / Пример чата

```
You> Привет! Как дела?
AI> Привет! У меня всё отлично, спасибо! Как я могу помочь тебе сегодня? 😊

You> Hello! How are you?
AI> Hello! I'm doing great, thanks for asking! How can I help you today? 😊

You> 你好！
AI> 你好！很高兴见到你！我能帮你什么吗？
```

---

## Supported Languages / Поддерживаемые языки

The AI can communicate in many languages, including:
AI может общаться на многих языках, включая:

- 🇬🇧 English
- 🇷🇺 Русский (Russian)
- 🇨🇳 中文 (Chinese)
- 🇯🇵 日本語 (Japanese)
- 🇰🇷 한국어 (Korean)
- 🇸🇦 العربية (Arabic)
- 🇪🇸 Español (Spanish)
- 🇫🇷 Français (French)
- 🇩🇪 Deutsch (German)
- And many more! / И многие другие!

---

## Technical Details / Технические детали

### Encoding Configuration
- Server: UTF-8 with error handling
- Docker: `LANG=C.UTF-8`, `LC_ALL=C.UTF-8`, `PYTHONIOENCODING=utf-8`
- Python: UTF-8 encoding with fallback to CP1251 for legacy systems

### Кодировка
- Сервер: UTF-8 с обработкой ошибок
- Docker: `LANG=C.UTF-8`, `LC_ALL=C.UTF-8`, `PYTHONIOENCODING=utf-8`
- Python: Кодировка UTF-8 с резервным вариантом CP1251 для старых систем
