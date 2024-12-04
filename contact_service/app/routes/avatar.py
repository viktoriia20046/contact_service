"""
Avatar Routes
This module handles avatar-related endpoints.
"""

from fastapi import APIRouter, File, UploadFile
import cloudinary
import cloudinary.uploader
import os

# Ініціалізація маршрутизатора
router = APIRouter()

@router.post("/upload-avatar/")
def upload_avatar(file: UploadFile = File(...)):
    """
    Upload an avatar to Cloudinary.

    This endpoint allows users to upload an avatar image to Cloudinary.
    The uploaded file is returned with its secure URL.

    :param file: The avatar file to upload.
    :type file: UploadFile
    :return: A dictionary containing the secure URL of the uploaded avatar.
    :rtype: dict
    """
    # Налаштування Cloudinary
    cloudinary.config(
        cloud_name=os.getenv("CLOUD_NAME"),
        api_key=os.getenv("CLOUD_API_KEY"),
        api_secret=os.getenv("CLOUD_API_SECRET")
    )
    
    # Завантаження файлу в Cloudinary
    upload_result = cloudinary.uploader.upload(file.file)
    
    # Повернення посилання на завантажений файл
    return {"url": upload_result["secure_url"]}