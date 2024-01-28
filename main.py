from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import smtplib
from email.mime.text import MIMEText
import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient
import mongo
import creds

client = MongoClient(mongo.mongoURL)
db = client["test"]

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
        email_user = creds.email
        email_password = creds.password

        # Creating the MIMEText object
        msg = MIMEText(message.message + "\n\n" +
                       message.name + "\n" + message.email)
        msg['Subject'] = "[Contact]"+f" {message.name} | "+message.subject
        msg['From'] = email_user

        # Establishing the connection to the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(email_user, email_password)

            # Sending the email
            server.sendmail(
                email_user, ["advaita@iiit-bh.ac.in", "dump@iiit-bh.ac.in"], msg.as_string())

        return JSONResponse(content={"message": "Email sent successfully"}, status_code=200)

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to send email: {str(e)}")


@app.post("/send-email/sponsor-us", tags=["Sponsor Us"])
async def send_email(message: Sponsor):
    try:
        # Your email and password for authentication
        email_user = creds.email
        email_password = creds.password

        # Creating the MIMEText object
        msg = MIMEText(message.proposal + "\n\n" + message.contact_person + "\n" +
                       message.designation + "\n" + message.email + "\n" + message.company_name)
        msg['Subject'] = "[Sponsor]"+f" {message.company_name}"
        msg['From'] = email_user

        # Establishing the connection to the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(email_user, email_password)

            # Sending the email
            server.sendmail(email_user, [
                            "advaita@iiit-bh.ac.in", "dump@iiit-bh.ac.in", "sponsoradvaita@iiit-bh.ac.in"], msg.as_string())

        return JSONResponse(content={"message": "Email sent successfully"}, status_code=200)

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to send email: {str(e)}")


@app.post("/prince/contact-us", tags=["Prince Portfolio Page"])
async def send_email(message: Message):
    try:
        # Your email and password for authentication
        email_user = creds.email
        email_password = creds.password

        # Creating the MIMEText object
        msg = MIMEText(message.message + "\n\n" +
                       message.name + "\n" + message.email)
        msg['Subject'] = "[Contact]"+f" {message.name} | "+message.subject
        msg['From'] = email_user

        # Establishing the connection to the SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(email_user, email_password)

            # Sending the email
            server.sendmail(email_user, [
                            "b221042@iiit-bh.ac.in", "princepious2003@gmail.com", "prakashprince2404@gmail.com"], msg.as_string())

        return JSONResponse(content={"message": "Email sent successfully"}, status_code=200)

    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to send email: {str(e)}")


@app.put("/checkin", tags=["Tickets"])
async def checkin(qr: str):
    try:
        doc = db.tickets.find_one({"qr": qr})
        if (doc["sold"] == True and doc["checkIn"] == False):
            db.tickets.update_one({"qr": qr}, {"$set": {"checkIn": True}})
            return JSONResponse(content={"message": "Checked In"}, status_code=200)
        else:
            return JSONResponse(content={False}, status_code=201)
    except Exception as e:
        return False


@app.put("/sell", tags=["Tickets"])
async def checkin(qr: str):
    try:
        doc = db.tickets.find_one({"qr": qr})
        if (doc["sold"] == False):
            db.tickets.update_one({"qr": qr}, {"$set": {"sold": True}})
            return JSONResponse(content={"message": "SOLD"}, status_code=200)
        else:
            return JSONResponse(content={False}, status_code=201)
    except Exception as e:
        return False


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
