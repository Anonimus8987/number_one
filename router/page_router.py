import os
import random
import string
import requests
from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse, HTMLResponse, Response, JSONResponse
from fastapi.templating import Jinja2Templates
from datetime import datetime

from model import *
from config import *

router = APIRouter(prefix='/page', tags=['page'])

templates = Jinja2Templates(directory=["templates", "templates/page"])


# Контакт
@router.post("/contact", response_class=HTMLResponse)
async def contact(request: Request, response: Response):
    try:
        form_data = await request.form()
        payload = {
            "chat_id": CHAT_ID, 
            "text": f"New message from Shortner:\nEmail: " + form_data.get("email") + "\nSubject: " + form_data.get("subject") + "\nMessage: " + form_data.get("message")
        }
        res = requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", headers={"Content-Type": "application/json"}, json=payload)
        if res.status_code == 200:
            context={
                "request": request,
                "bg": request.url_for("static", path="home.jpg"),
                "message": "Message sent successfully!",
                "auth": bool(1)
            }
        else:
            context={
                "request": request,
                "bg": request.url_for("static", path="home.jpg"),
                "message": f"Error sending message: {res.status_code} {res.text}",
                "auth": bool(1)
            }
        return templates.TemplateResponse("contact.html", context)
    except Exception as e:
        print(e)
        return RedirectResponse(f"{DOMAIN}/error")

@router.get("/contact", response_class=HTMLResponse)
async def contact(request: Request, response: Response):
    context={
        "request": request,
        "bg": request.url_for("static", path="home.jpg"),
        "auth": bool(1)
    }
    return templates.TemplateResponse("contact.html", context)

# Политика конфиденциальности
@router.get("/privacy-policy", response_class=HTMLResponse)
async def contact(request: Request, response: Response):
    context={
        "request": request,
        "bg": request.url_for("static", path="home.jpg"),
        "auth": bool(1)
    }
    return templates.TemplateResponse("privacy.html", context)

# Условия и положения
@router.get("/terms-and-condition", response_class=HTMLResponse)
async def contact(request: Request, response: Response):
    context={
        "request": request,
        "bg": request.url_for("static", path="home.jpg"),
        "auth": bool(1)
    }
    return templates.TemplateResponse("terms.html", context)

## Страница ошибки
@router.get("/error", response_class=HTMLResponse)
async def error(request: Request):
    context={
        "request": request,
        "bg": request.url_for("static", path="error.jpg")
    }
    return templates.TemplateResponse("error.html", context)
