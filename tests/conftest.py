import pytest
import json
import pathlib
import shutil
from config import env


@pytest.fixture(scope="session")
def test_tools():
    """
    Data for work with all the database
    :return:  BD record list
    """
    tools = [
        {"id": 1, "tool": "Ansible", "url": "https://ansible.com"},
        {"id": 2, "tool": "Bitbucket", "url": "https://bitbucket.com"},
        {"id": 3, "tool": "Jenkins", "url": "https://jenkins.ru"},
    ]
    return tools


@pytest.fixture(scope="session")
def test_new_tool():
    """
    Data for working with one recording of the database
    :return: correctly executed entry in the database
    """
    tool = {"id": 5, "tool": "GitLab", "url": "https://gitlab.ru"}
    return tool


@pytest.fixture(scope="session")
def db(tmp_path_factory, test_tools):
    """
    Creating a test database. YIELD. Removing the test database
    :param tmp_path_factory: Temporary catalog within the session
    :param test_tools: List of CI/CD tools
    """
    tmp_dir_db = tmp_path_factory.mktemp("db")
    with open(tmp_dir_db / "test_tools.json", "w", encoding="utf8") as stream:
        json.dump(test_tools, stream, ensure_ascii=False, indent=4)

    env.JSON_DB_PATH = str(tmp_dir_db / "test_tools.json")

    yield

    # We delete a temporary catalog for tests
    if pathlib.Path(str(tmp_path_factory.getbasetemp())).exists():
        shutil.rmtree(str(tmp_path_factory.getbasetemp()))
