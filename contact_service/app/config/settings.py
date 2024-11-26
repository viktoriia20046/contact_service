import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_CONFIG = {
    "host": os.getenv("EMAIL_HOST"),
    "port": os.getenv("EMAIL_PORT"),
    "user": os.getenv("EMAIL_USER"),
    "password": os.getenv("EMAIL_PASSWORD"),
}