FROM python:3.11-slim

WORKDIR /app

# Install system dependencies via playwright install-deps (handles package names automatically)
RUN apt-get update && apt-get install -y \
    wget curl gnupg \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Let playwright install chromium + all its own deps (avoids hardcoded package names)
RUN playwright install chromium --with-deps

COPY agent.py .

CMD ["python", "agent.py"]
