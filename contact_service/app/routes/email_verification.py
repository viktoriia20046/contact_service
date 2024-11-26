from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import EmailStr
import smtplib

router = APIRouter()

@router.post("/send-email/")
def send_verification_email(background_tasks: BackgroundTasks, email: EmailStr):
    try:
        background_tasks.add_task(send_email, email)
        return {"message": "Verification email sent"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def send_email(email: str):
    import os
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    smtp = smtplib.SMTP(os.getenv("EMAIL_HOST"), int(os.getenv("EMAIL_PORT")))
    smtp.starttls()
    smtp.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASSWORD"))

    msg = MIMEMultipart()
    msg["From"] = os.getenv("EMAIL_USER")
    msg["To"] = email
    msg["Subject"] = "Verify your email"
    msg.attach(MIMEText(f"Click the link to verify: http://127.0.0.1:8000/verify-email?email={email}", "plain"))

    smtp.send_message(msg)
    smtp.quit()