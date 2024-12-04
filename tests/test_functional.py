import sys
import os

# Додавання кореневого каталогу до системного шляху
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

import pytest
from fastapi.testclient import TestClient
from main import app 

# Ініціалізація клієнта для тестування
client = TestClient(app)

@pytest.fixture
def test_file():
    """
    Фікстура для підготовки тестового файлу
    """
    return {"file": ("avatar.jpg", b"test data", "image/jpeg")}

def test_upload_avatar_functional(test_file):
    """
    Функціональний тест для перевірки маршруту /upload-avatar/
    """
    response = client.post("/upload-avatar/", files=test_file)
    assert response.status_code == 200
    assert "url" in response.json()