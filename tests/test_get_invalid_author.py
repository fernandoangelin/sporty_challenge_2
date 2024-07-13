import requests

from src.setup.base_values import BASE_URL
from src.setup.base_values import AUTHOR_ENDPOINT

AUTHOR = "My Name Is"

def test_get_poems_by_invalid_author():
    response = requests.get(f"{BASE_URL}{AUTHOR_ENDPOINT}/{AUTHOR}")
    assert response.status_code == 200
    error_data = response.json()
    assert isinstance(error_data, dict)

    assert "status" and "reason" in error_data

    assert isinstance(error_data["status"], int)
    assert error_data["status"] == 404
    assert isinstance(error_data["reason"], str)
    assert error_data["reason"] == "Not found"
