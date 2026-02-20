from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import qrcode
import io
import base64
from pathlib import Path

app = FastAPI()

# Determine the base directory (where main.py is located)
BASE_DIR = Path(__file__).resolve().parent

# Mount the public directory using the absolute path
app.mount("/public", StaticFiles(directory=BASE_DIR / "public"), name="public")

class WifiCredentials(BaseModel):
    ssid: str
    password: str
    encryption: str = "WPA"  # Default to WPA/WPA2

@app.post("/generate")
async def generate_qr(creds: WifiCredentials):
    # WIFI:S:MySSID;T:WPA;P:MyPass;;
    wifi_data = f"WIFI:S:{creds.ssid};T:{creds.encryption};P:{creds.password};;"
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(wifi_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save to memory buffer
    buffered = io.BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    
    return {"qr_image": f"data:image/png;base64,{img_str}"}

@app.get("/")
async def read_index():
    from fastapi.responses import FileResponse
    # Serve index.html using the absolute path
    return FileResponse(BASE_DIR / 'public/index.html')

if __name__ == "__main__":
    import os
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
