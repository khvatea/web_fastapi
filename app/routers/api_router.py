from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import JSONResponse
from tools import Tools
from schemas import ToolsModel

router = APIRouter(tags=["api"])
templates = Jinja2Templates(directory="app/templates")


@router.get(
    "/entities",
    response_class=JSONResponse,
    summary="Получение списка CI/CD инструментов",
    description="Список CI/CD инструментов содержит элементы,"
    "каждый из которых содержит:<br>"
    "<b>ID</b> - уникальный номер записи в базе<br>"
    "<b>tool</b> - название инструмента<br>"
    "<b>url</b> - ссылка на ресурс инструмента",
)
async def entities():
    """
    Obtaining a CI/CD list
    :return: CI/CD list in json
    """
    tools = Tools("resources/tools.json").get_entities()
    return {"tools": tools}


@router.get(
    "/entity/{item_id}",
    response_class=JSONResponse,
    summary="Получение описания определенного CI/CD инструмента",
    description="Описание CI/CD инструмента содержит:<br>"
    "<b>ID</b> - уникальный номер записи в базе<br>"
    "<b>tool</b> - название инструмента<br>"
    "<b>url</b> - ссылка на ресурс инструмента",
)
async def entity(item_id: int):
    """
    Obtaining a description of a certain element from the list
    :param item_id: ID records
    :return: Status and description of the element in JSON format
    """
    tool = Tools("resources/tools.json").get_entity(item_id)
    if tool:
        return {"status": "success", "item": tool}

    return JSONResponse(
        content={"status": "failed", "message": f"указанный ID={item_id} не найден"},
        status_code=422,
    )


@router.post(
    "/add",
    response_class=JSONResponse,
    summary="Добавление нового CI/CD инструмента",
    description="Описание CI/CD инструмента содержит:<br>"
    "<b>ID</b> - уникальный номер записи в базе<br>"
    "<b>tool</b> - название инструмента<br>"
    "<b>url</b> - ссылка на ресурс инструмента",
)
async def add_entity(item: ToolsModel):
    """
    Adding an entry to json
    :param item: Object according to the Toolsmodel scheme
    :return: The status of an operation performed
    """
    if Tools("resources/tools.json").add_entity(item) == 0:
        return {
            "status": "success",
            "message": "Элемент успешно добавлен",
            "item": item,
        }
    else:
        return JSONResponse(
            content={"status": "failed", "message": "ID дублирован"},
            status_code=422,
        )
