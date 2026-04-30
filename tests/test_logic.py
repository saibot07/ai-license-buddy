import pytest
from license_recommender.logic import recommend_license

def test_recommend_license():
    assert recommend_license("library", "yes", "yes") == "MIT License"
    assert recommend_license("library", "no", "yes") == "GPLv3"
    assert recommend_license("application", "yes", "no") == "Non-Commercial Creative Commons"

def test_invalid_inputs():
    with pytest.raises(ValueError):
        recommend_license("library", "invalid", "yes")