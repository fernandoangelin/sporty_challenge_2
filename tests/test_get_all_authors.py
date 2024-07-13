import requests

from src.setup.base_values import BASE_URL
from src.setup.base_values import AUTHOR_ENDPOINT

def test_get_all_authors():
    response = requests.get(f"{BASE_URL}{AUTHOR_ENDPOINT}")
    assert response.status_code == 200
    authors_dict = response.json()
    assert isinstance(authors_dict, dict)
    assert "authors" in authors_dict
    assert isinstance(authors_dict["authors"], list)
