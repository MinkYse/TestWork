from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="app/static/templates")
home_pages_router = APIRouter()


@home_pages_router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
