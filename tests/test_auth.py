from fastapi.testclient import TestClient
from main import app  # your FastAPI app

client = TestClient(app)
