import unittest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from app.routes.avatar import upload_avatar
from main import app

client = TestClient(app)

class TestAvatarRoutes(unittest.TestCase):
    @patch("app.routes.avatar.cloudinary.uploader.upload")
    def test_upload_avatar(self, mock_upload):
        # Мок для Cloudinary
        mock_upload.return_value = {"secure_url": "https://example.com/avatar.jpg"}

        # Тестовий файл для завантаження
        test_file = {"file": ("avatar.jpg", b"test data", "image/jpeg")}
        response = client.post("/upload-avatar/", files=test_file)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"url": "https://example.com/avatar.jpg"})

if __name__ == "__main__":
    unittest.main()