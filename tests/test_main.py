import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app
import base64

@pytest.mark.asyncio
async def test_read_index():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == 200
    assert "html" in response.headers["content-type"]

@pytest.mark.asyncio
async def test_generate_qr_success():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {
            "ssid": "MyWiFi",
            "password": "mypassword",
            "encryption": "WPA"
        }
        response = await ac.post("/generate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "qr_image" in data
    assert data["qr_image"].startswith("data:image/png;base64,")

@pytest.mark.asyncio
async def test_generate_qr_no_password():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {
            "ssid": "PublicWiFi",
            "password": "",
            "encryption": "nopass"
        }
        response = await ac.post("/generate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "qr_image" in data

@pytest.mark.asyncio
async def test_generate_qr_missing_ssid():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {
            "password": "mypassword",
            "encryption": "WPA"
        }
        response = await ac.post("/generate", json=payload)
    assert response.status_code == 422  # Pydantic validation error

@pytest.mark.asyncio
async def test_generate_qr_special_characters():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {
            "ssid": "My WiFi !@#$%^&*()",
            "password": "pass word 123",
            "encryption": "WPA"
        }
        response = await ac.post("/generate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "qr_image" in data

@pytest.mark.asyncio
async def test_generate_qr_long_strings():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {
            "ssid": "A" * 100,
            "password": "B" * 100,
            "encryption": "WPA"
        }
        response = await ac.post("/generate", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "qr_image" in data

@pytest.mark.asyncio
async def test_generate_qr_invalid_json():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post(
            "/generate", 
            content="invalid json", 
            headers={"Content-Type": "application/json"}
        )
    assert response.status_code == 422
# FastAPI returns 422 for malformed JSON too usually, or 400 if it fails before validation.
