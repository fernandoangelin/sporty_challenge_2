import requests

from src.setup.base_values import BASE_URL
from src.setup.base_values import AUTHOR_ENDPOINT

AUTHOR = "Shakespeare"
AUTHOR_NAME = "William Shakespeare"

def test_get_poems_by_author():
    response = requests.get(f"{BASE_URL}{AUTHOR_ENDPOINT}/{AUTHOR}")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert data[0]["author"] == AUTHOR_NAME
