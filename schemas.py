from pydantic import BaseModel


class ToolsModel(BaseModel):
    id: int
    tool: str
    url: str
