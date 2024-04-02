from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse, HTMLResponse, Response, JSONResponse
from fastapi.templating import Jinja2Templates

from model import *
from config import *

router = APIRouter(prefix='/admin', tags=['admin'])

templates = Jinja2Templates(directory=["templates", "templates/admin"])



# Панель приборов
@router.get("/admin/dashboard", response_class=HTMLResponse)
async def admin(request: Request, response: Response):
    context={
        "request": request,
        "bg": request.url_for("static", path="home.jpg"),
        "auth": bool(1)
    }
    return templates.TemplateResponse("adminDashboard.html", context)

@router.post("/admin/dashboard", response_class=HTMLResponse)
async def admin(request: Request, response: Response):
    context={
        "request": request,
        "bg": request.url_for("static", path="home.jpg"),
        "auth": bool(1)
    }
    return templates.TemplateResponse("adminDashboard.html", context)
    