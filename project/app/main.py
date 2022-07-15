from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.exceptions import HTTPException
from fastapi.staticfiles import StaticFiles

from .routes.homepage import home_pages_router
from .routes.ws import websockets_router


def include_router(app):
    app.include_router(home_pages_router)
    app.include_router(websockets_router)


def configure_static(app):
    app.mount("/static", StaticFiles(directory="app/static"), name="static")


def include_error_handler(app):
    templates = Jinja2Templates(directory="app/static/templates")

    @app.exception_handler(HTTPException)
    async def exception(request: Request, exc: HTTPException):
        if exc.status_code == 404:
            return templates.TemplateResponse("404.html", {"request": request})


def start_application():
    app = FastAPI(title='Messages', version='1.0')
    configure_static(app)
    include_router(app)
    include_error_handler(app)
    return app


app = start_application()

