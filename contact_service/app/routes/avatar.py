from fastapi import APIRouter, File, UploadFile
import cloudinary
import cloudinary.uploader
import os

router = APIRouter()

@router.post("/upload-avatar/")
def upload_avatar(file: UploadFile = File(...)):
    cloudinary.config(
        cloud_name=os.getenv("CLOUD_NAME"),
        api_key=os.getenv("CLOUD_API_KEY"),
        api_secret=os.getenv("CLOUD_API_SECRET"),
    )
    upload_result = cloudinary.uploader.upload(file.file)
    return {"url": upload_result["secure_url"]}