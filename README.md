# GuestPass

GuestPass is a simple, local-first web application that generates printable WiFi access cards with QR codes for your guests.

## Features

- **Instant QR Code Generation**: Enter your WiFi credentials efficiently.
- **Privacy Focused**: Runs entirely locally; no data leaves your network.
- **Printable Cards**: Generates a clean, card-sized layout for printing.
- **Standard Security**: Supports WPA/WPA2 authentication methods.

## Getting Started

### Prerequisites

- Python 3.8+
- [Optional] Docker

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd guest-pass
   ```

2. **Set up a virtual environment**
   ```bash
   python -m venv .venv
   # Windows
   .venv\Scripts\activate
   # macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r app/requirements.txt
   ```

### Usage

Run the application:

```bash
python app/main.py
```

Open your browser and navigate to:
[http://127.0.0.1:8000](http://127.0.0.1:8000)

### Docker Support

To run using Docker:

1. Navigate to the app directory:
   ```bash
   cd app
   ```

2. Build and run the container:
   ```bash
   docker build -t guest-pass .
   docker run -p 8000:8000 guest-pass
   ```

## License

[MIT](LICENSE)
