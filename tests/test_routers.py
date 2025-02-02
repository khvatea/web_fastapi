from fastapi.testclient import TestClient
import pytest
import json
from main import app


client = TestClient(app)


def test_api_entities(db, test_tools):
    """
    Route testing "/api/entities".
    :param db: provision of a database for testing a request
    :param test_tools: Standard list for comparison
    :return:
    """
    response = client.get("/api/entities")
    assert response.status_code == 200
    assert response.json()["tools"] == test_tools


@pytest.mark.parametrize("item", [1, 2, 3])
def test_api_entity(db, test_tools, item):
    """
    Checking the entry of the tool received by the API into the standard tool list
    :param db: provision of a database for testing a request
    :param test_tools: Standard list for comparison
    :param item: Number of the list element being checked
    :return:
    """
    response = client.get(f"/api/entity/{item}")
    assert response.status_code == 200
    assert response.json()["item"] in test_tools


def test_api_entity_failed(db):
    """
    Checking a non -existing element in the list
    :param db: provision of a database for testing a request
    :return:
    """
    response = client.get(f"/api/entity/45")
    # Decoding the byte line in a regular line
    decoded_string = response.content.decode("utf-8")
    # We convert a line into a dictionary
    data_dict = json.loads(decoded_string)

    assert data_dict["status"] == "failed"
    assert response.status_code == 422


def test_api_entity_add(db, test_new_tool):
    """
    Check for adding a new element to the database
    :param db: provision of a database for testing a request
    :param test_new_tool: correctly executed entry
    :return:
    """
    response = client.post("/api/add", json=test_new_tool)
    decoded_string = response.content.decode("utf-8")
    data_dict = json.loads(decoded_string)

    assert data_dict["status"] == "success"
    assert response.status_code == 201
