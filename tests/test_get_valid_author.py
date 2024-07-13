import requests

from src.setup.base_values import BASE_URL
from src.setup.base_values import AUTHOR_ENDPOINT

AUTHOR = "Shakespeare"
AUTHOR_NAME = "William Shakespeare"

def test_get_poems_by_author():
    response = requests.get(f"{BASE_URL}{AUTHOR_ENDPOINT}/{AUTHOR}")
    assert response.status_code == 200
    poems_list = response.json()
    assert len(poems_list) > 0
    assert isinstance(poems_list, list)

    for poem in poems_list:
        assert poem["author"] == AUTHOR_NAME
        assert "lines" in poem
        assert isinstance(poem["lines"], list)
