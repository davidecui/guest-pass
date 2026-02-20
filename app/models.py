from pydantic import BaseModel

class WifiCredentials(BaseModel):
    ssid: str
    password: str
    encryption: str = "WPA"  # Default to WPA/WPA2
