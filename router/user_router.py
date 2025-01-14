from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse, HTMLResponse, Response, JSONResponse
from fastapi.templating import Jinja2Templates

from model import *
from config import *

router = APIRouter(prefix='/users', tags=['users'])

templates = Jinja2Templates(directory=["templates/user", "templates"])

# Панель приборов
## Основной
@router.get("/dashboard", response_class=HTMLResponse)
async def dashboardHome(request: Request):
    context={
        "request": request,
        "bg": request.url_for("static", path="home.jpg"),
        "page": 1,
        "auth": bool(1)
    }
    return templates.TemplateResponse("dashboard.html", context)

@router.post("/dashboard", response_class=HTMLResponse)
async def dashboardHome(request: Request):
    context = {
        "request": request,
        "bg": request.url_for("static", path="home.jpg"),
        "page": 1,
        "auth": bool(1)
    }
    return templates.TemplateResponse("dashboard.html", context)

## Профиль
@router.get("/dashboard/profile", response_class=HTMLResponse)
async def dashboardProfile(request: Request):
    context={
        "request": request,
        "bg": request.url_for("static", path="home.jpg"),
        "page": 2,
        "auth": bool(1)
    }
    return templates.TemplateResponse("dashboardProfile.html", context)

@router.post("/dashboard/profile", response_class=HTMLResponse)
async def dashboardProfile(request: Request):
    context = {
        "request": request,
        "bg": request.url_for("static", path="home.jpg"),
        "page": 2,
        "auth": bool(1)
    }
    return templates.TemplateResponse("dashboardProfile.html", context)

## Настройки
@router.get("/dashboard/settings", response_class=HTMLResponse)
async def dashboardSettings(request: Request):
    context={
        "request": request,
        "bg": request.url_for("static", path="home.jpg"),
        "page": 3,
        "auth": bool(1)
    }
    return templates.TemplateResponse("dashboardSettings.html", context)

@router.post("/dashboard/settings", response_class=HTMLResponse)
async def dashboardSettings(request: Request):
    context = {
        "request": request,
        "bg": request.url_for("static", path="home.jpg"),
        "page": 3,
        "auth": bool(1)
    }
    return templates.TemplateResponse("dashboardSettings.html", context)

## Сократить
@router.get("/dashboard/shorten", response_class=HTMLResponse)
async def dashboardShorten(request: Request):
    shorts = []

    agg = [   
        {'$match': {'secured': 0}},
        {'$facet': { 'sh': [{ '$project': { "short": "$short", "visits": "$views", "report": "$report", "created_at": "$created_at", "url": "$url" } }] }} 
    ]

    try:
        collection = mongodb.aggregate(agg)
    except:
        pass
    async for doc in collection:
        shorts = doc['sh']

    context={
        "request": request,
        "bg": request.url_for("static", path="home.jpg"),
        "page": 4,
        "domain": DOMAIN,
        "shorts": shorts,
        "auth": bool(1)
    }
    return templates.TemplateResponse("dashboardShorten.html", context)

@router.post("/dashboard/shorten", response_class=HTMLResponse)
async def dashboardShorten(request: Request):
    context = {
        "request": request,
        "bg": request.url_for("static", path="home.jpg"),
        "page": 4,
        "auth": bool(1)
    }
    return templates.TemplateResponse("dashboardShorten.html", context)


# Документация (API)
@router.get("/dev/documentation", response_class=HTMLResponse)
async def documentation(request: Request):
    context={
        "request": request,
        "bg": request.url_for("static", path="home.jpg"),
        "page": 5,
        "auth": bool(1)
    }
    return templates.TemplateResponse("dashboardDocs.html", context)

@router.post("/dev/documentation", response_class=HTMLResponse)
async def documentation(request: Request):
    context = {
        "request": request,
        "bg": request.url_for("static", path="home.jpg"),
        "page": 5,
        "auth": bool(1)
    }
    return templates.TemplateResponse("dashboardDocs.html", context)
