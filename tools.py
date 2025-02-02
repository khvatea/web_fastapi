import json
from schemas import ToolsModel


class Tools:
    """
    Class for working with json records CI/CD tools
    """

    def __init__(self, file: str):
        """
        Initialization of the Tools object
        :param file: The path to the JSON-file with a description of the tools
        """
        self.file = file

    def get_entities(self) -> list:
        """
        Open a json file with a list of tools
        :return: list of tools
        """
        tools = []
        # Open file, read and pass to list object
        with open(self.file, "r", encoding="utf8") as stream:
            for tool in json.load(stream):
                try:
                    model = ToolsModel(**tool).model_dump()
                    tools.append(model)
                except Exception as e:
                    print(f"Ошибка валидации записи в файле({self.file}): {e}")

        return tools

    def get_entity(self, item_id: int) -> dict:
        """
        Get an entity from a common list of tools
        :param item_id: ID entity
        :return: All properties of entity
        """
        tools = self.get_entities()

        for i, tool in enumerate(tools):
            if tool["id"] == item_id:
                return tools[i]

    def add_entity(self, new_item: ToolsModel) -> int:
        """
        Add an entry to the CI/CD list
        :param new_item: Properties of entity
        :return: 1 - there is duplication. 0 - Record is added successfully
        """
        tools = self.get_entities()

        for tool in tools:
            if tool["id"] == new_item.id:
                return 1

        tools.append(new_item.model_dump())
        with open(self.file, "w", encoding="utf8") as stream:
            json.dump(tools, stream, ensure_ascii=False, indent=4)

        return 0
