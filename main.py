from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import smtplib
from email.mime.text import MIMEText
import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    subject: str
    message: str
    name: str
    email: str

class Sponsor(BaseModel):
    company_name: str
    proposal: str
    contact_person: str
    designation: str
    email: str

@app.post("/send-email/contact-us", tags=["Contact Us"])
async def send_email(message: Message):
    try:
        # Your email and password for authentication
        email_user = "jarvisnayak@gmail.com"
        email_password = "umlysbykyfpjqypr"

        # Creating the MIMEText object
        msg = MIMEText(message.message + "\n\n" + message.name + "\n" + message.email)
        msg['Subject'] = "[Contact]"+f" {message.name} | "+message.subject
        msg['From'] = email_user

        # Establishing the connection to the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(email_user, email_password)

            # Sending the email
            server.sendmail(email_user, ["advaita@iiit-bh.ac.in", "dump@iiit-bh.ac.in"], msg.as_string())

        return JSONResponse(content={"message": "Email sent successfully"}, status_code=200)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")
    
@app.post("/send-email/sponsor-us", tags=["Sponsor Us"])
async def send_email(message: Sponsor):
    try:
        # Your email and password for authentication
        email_user = "jarvisnayak@gmail.com"
        email_password = "umlysbykyfpjqypr"

        # Creating the MIMEText object
        msg = MIMEText(message.proposal + "\n\n" + message.contact_person + "\n" + message.designation+ "\n" + message.email + "\n" + message.company_name)
        msg['Subject'] = "[Sponsor]"+f" {message.company_name}"
        msg['From'] = email_user

        # Establishing the connection to the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(email_user, email_password)

            # Sending the email
            server.sendmail(email_user, ["advaita@iiit-bh.ac.in", "dump@iiit-bh.ac.in", "sponsoradvaita@iiit-bh.ac.in"], msg.as_string())

        return JSONResponse(content={"message": "Email sent successfully"}, status_code=200)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")
    
@app.post("/prince/contact-us", tags=["Prince Portfolio Page"])
async def send_email(message: Message):
    try:
        # Your email and password for authentication
        email_user = "jarvisnayak@gmail.com"
        email_password = "umlysbykyfpjqypr"

        # Creating the MIMEText object
        msg = MIMEText(message.message + "\n\n" + message.name + "\n" + message.email)
        msg['Subject'] = "[Contact]"+f" {message.name} | "+message.subject
        msg['From'] = email_user

        # Establishing the connection to the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(email_user, email_password)

            # Sending the email
            server.sendmail(email_user, ["advaita@iiit-bh.ac.in", "dump@iiit-bh.ac.in"], msg.as_string())

        return JSONResponse(content={"message": "Email sent successfully"}, status_code=200)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to send email: {str(e)}")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)