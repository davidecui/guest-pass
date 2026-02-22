FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Use shell form of CMD to ensure environment variable expansion
CMD uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}
