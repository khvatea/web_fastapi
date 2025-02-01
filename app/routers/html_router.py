from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from tools import Tools

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/", response_class=HTMLResponse)
async def route_index(request: Request):
    """
    Processing of the root route
    :param request:
    :return: Generated page on the template 'index.html'
    """
    tools = Tools("resources/tools.json").get_entities()
    return templates.TemplateResponse(
        "index.html", {"request": request, "tools": tools}
    )


@router.get("/about", response_class=HTMLResponse)
async def route_about(request: Request):
    """
    Processing of the '/about' route
    :param request:
    :return: Generated page on the template 'about.html'
    """
    return templates.TemplateResponse("about.html", {"request": request})
