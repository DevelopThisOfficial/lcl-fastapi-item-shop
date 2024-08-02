from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

CURRDIR = os.path.dirname(__file__)
templates = Jinja2Templates(os.path.join(CURRDIR, "templates"))


app = FastAPI(
    title="DevelopThis Items",
    description="A simple example of displaying items from FastAPI.",
)

app.mount(
    "/static",
    StaticFiles(directory=os.path.join(os.path.dirname(CURRDIR), "static")),
    name="static",
)


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="index.html")


@app.get("/api/items", tags=["Items"])
async def get_items():
    return [
        {
            "item_name": "Tutoring",
            "price": 45,
            "description": "Private tutoring offered by one of our many talented staff members.",
        },
        {
            "item_name": "Website Build",
            "price": 1000,
            "description": "Have our professional developers, develop your site!",
        },
    ]
