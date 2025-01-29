from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

tools = [
    {"id": 1, "tool": "Ansible", "url": "https://ansible.com"},
    {
        "id": 2,
        "tool": "Nexus",
        "url": "https://www.sonatype.com/products/sonatype-nexus-repository",
    },
    {
        "id": 3,
        "tool": "Bitbucket",
        "url": "https://bitbucket.com"
    },
    {
        "id": 4,
        "tool": "SonarQube","url": "https://sonarqube.com"
    },
]


@router.get("/", response_class=HTMLResponse)
async def route_index(request: Request):
    """
    Processing of the root route
    :param request:
    :return: Generated page on the template 'index.html'
    """
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
