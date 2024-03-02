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
import datetime

client = MongoClient(mongo.mongoURL)
db = client["production"]

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


@app.put("/checkout", tags=["Tickets"])
async def checkin(qr: str):
    try:
        doc = db.tickets.find_one({"qr": qr})
        db.tickets.update_one({"qr": qr}, {
            "$set": {"day0Checkin": False, "day1Checkin": False, "day2Checkin": False, "day3Checkin": False}})
        return JSONResponse(content={"message": "Checked Out"}, status_code=200)
    except Exception as e:
        return False


@app.put("/checkin/day0", tags=["Tickets"])
async def checkin(qr: str):
    try:
        doc = db.tickets.find_one({"qr": qr})
        if (doc["day0"] == True and doc["day0Checkin"] == False):
            db.tickets.update_one({"qr": qr}, {
                                  "$set": {"day0Checkin": True, "day0CheckInAt": datetime.datetime.now()}})
            return JSONResponse(content={"message": "Checked In"}, status_code=200)
        else:
            return JSONResponse(content={False}, status_code=201)
    except Exception as e:
        return False


@app.put("/checkin/day1", tags=["Tickets"])
async def checkin(qr: str):
    try:
        doc = db.tickets.find_one({"qr": qr})
        if (doc["day1"] == True and doc["day1Checkin"] == False):
            db.tickets.update_one({"qr": qr}, {
                                  "$set": {"day1Checkin": True, "day1CheckInAt": datetime.datetime.now()}})
            return JSONResponse(content={"message": "Checked In"}, status_code=200)
        else:
            return JSONResponse(content={False}, status_code=201)
    except Exception as e:
        return False


@app.put("/checkin/day2", tags=["Tickets"])
async def checkin(qr: str):
    try:
        doc = db.tickets.find_one({"qr": qr})
        if (doc["day2"] == True and doc["day2Checkin"] == False):
            db.tickets.update_one({"qr": qr}, {
                                  "$set": {"day2Checkin": True, "day2CheckInAt": datetime.datetime.now()}})
            return JSONResponse(content={"message": "Checked In"}, status_code=200)
        else:
            return JSONResponse(content={False}, status_code=201)
    except Exception as e:
        return False


@app.put("/checkin/day3", tags=["Tickets"])
async def checkin(qr: str):
    try:
        doc = db.tickets.find_one({"qr": qr})
        if (doc["day3"] == True and doc["day3Checkin"] == False):
            db.tickets.update_one({"qr": qr}, {
                                  "$set": {"day3Checkin": True, "day3CheckInAt": datetime.datetime.now()}})
            return JSONResponse(content={"message": "Checked In"}, status_code=200)
        else:
            return JSONResponse(content={False}, status_code=201)
    except Exception as e:
        return False


@app.put("/sell/allDay", tags=["Tickets"])
async def checkin(qr: str, name: str, email: str, phone: str, comments: str = ""):
    try:
        if (True):
            db.tickets.insert_one(
                {"qr": qr, "day0": True, "day1": True, "day2": True, "day3": True, "AllDaySoldAt": datetime.datetime.now(
                ), "name": name, "email": email, "phone": phone, "comments": comments}
            )
            db.logs.insert_one(
                {"action": f'All Day ticket sold at {datetime.datetime.now()}', 'name': name, 'email': email, 'phone': phone, 'comments': comments, 'qr': qr})
            return JSONResponse(content={"message": "SOLD"}, status_code=200)
        else:
            return JSONResponse(content={False}, status_code=201)
    except Exception as e:
        return False


@app.put("/sell/day0", tags=["Tickets"])
async def checkin(qr: str, name: str, email: str, phone: str, comments: str = ""):
    try:
        doc = db.tickets.find_one({"qr": qr})
        if (doc["day0"] == False and doc["verify"] == True):
            db.tickets.insert_one({"qr": qr, "day0": True, "day0SoldAt": datetime.datetime.now(
            ), "name": name, "email": email, "phone": phone, "comments": comments})
            db.logs.insert_one(
                {"action": f'Day 0 ticket sold at {datetime.datetime.now()}', 'name': name, 'email': email, 'phone': phone, 'comments': comments, 'qr': qr})
            return JSONResponse(content={"message": "SOLD"}, status_code=200)
        else:
            return JSONResponse(content={False}, status_code=201)
    except Exception as e:
        return False


@app.put("/sell/day1", tags=["Tickets"])
async def checkin(qr: str, name: str, email: str, phone: str, comments: str = ""):
    try:
        doc = db.tickets.find_one({"qr": qr})
        if (doc["day1"] == False and doc["verify"] == True):
            db.tickets.update_one(
                {"qr": qr}, {"$set": {"day1": True, "day1SoldAt": datetime.datetime.now(), "name": name, "email": email, "phone": phone, "comments": comments}})
            db.logs.insert_one(
                {"action": f'Day 1 ticket sold at {datetime.datetime.now()}', 'name': name, 'email': email, 'phone': phone, 'comments': comments, 'qr': qr})
            return JSONResponse(content={"message": "SOLD"}, status_code=200)
        else:
            return JSONResponse(content={False}, status_code=201)
    except Exception as e:
        return False


@app.put("/sell/day2", tags=["Tickets"])
async def checkin(qr: str, name: str, email: str, phone: str, comments: str = ""):
    try:
        doc = db.tickets.find_one({"qr": qr})
        if (doc["day2"] == False and doc["verify"] == True):
            db.tickets.update_one(
                {"qr": qr}, {"$set": {"day2": True, "day2SoldAt": datetime.datetime.now(), "name": name, "email": email, "phone": phone, "comments": comments}})
            db.logs.insert_one(
                {"action": f'Day 2 ticket sold at {datetime.datetime.now()}', 'name': name, 'email': email, 'phone': phone, 'comments': comments, 'qr': qr})
            return JSONResponse(content={"message": "SOLD"}, status_code=200)
        else:
            return JSONResponse(content={False}, status_code=201)
    except Exception as e:
        return False


@app.put("/sell/day3", tags=["Tickets"])
async def checkin(qr: str, name: str, email: str, phone: str, comments: str = ""):
    try:

        if (True):
            db.tickets.insert_one(
                {"qr": qr, "day0": True, "day1": True, "day2": True, "day3": True, "AllDaySoldAt": datetime.datetime.now(
                ), "name": name, "email": email, "phone": phone, "comments": comments}
            )
            db.logs.insert_one(
                {"action": f'Day 3 ticket sold at {datetime.datetime.now()}', 'name': name, 'email': email, 'phone': phone, 'comments': comments, 'qr': qr})
            return JSONResponse(content={"message": "SOLD"}, status_code=200)
        else:
            return JSONResponse(content={False}, status_code=201)
    except Exception as e:
        return False


@app.put("/verify", tags=["Tickets"])
async def checkin(qr: str):
    try:
        doc = db.tickets.find_one({"qr": qr})
        if (doc["verify"] == False):
            db.tickets.update_one(
                {"qr": qr}, {"$set": {"verify": True, "verifiedAt": datetime.datetime.now()}})
            db.logs.insert_one(
                {"action": f'Ticket verified at {datetime.datetime.now()}'})
            return JSONResponse(content={"message": "VERIFIED"}, status_code=200)
        else:
            return JSONResponse(content={False}, status_code=201)
    except Exception as e:
        return False


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8001, reload=True)
