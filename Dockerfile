FROM python:3.11-slim

# Set UTF-8 locale for proper Cyrillic and Unicode support
ENV LANG=C.UTF-8 \
    LC_ALL=C.UTF-8 \
    PYTHONIOENCODING=utf-8

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Create necessary directories
RUN mkdir -p /app/logs /app/data

# Expose telnet port
EXPOSE 2323

# Run the BBS server
CMD ["python", "bbs_server.py"]
