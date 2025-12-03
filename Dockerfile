# Use official Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port (Render assigns dynamically)
EXPOSE 8050

# Run with gunicorn (Render provides PORT env variable)
# Using 2 workers for free tier memory limits
# Shell form to ensure PORT variable expansion works
CMD ["sh", "-c", "gunicorn app:server --bind 0.0.0.0:${PORT:-8050} --workers 2 --timeout 120 --max-requests 1000 --max-requests-jitter 50"]
