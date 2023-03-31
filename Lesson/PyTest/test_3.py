import pytest


# @pytest.fixture
# def first_entry():
#     return "a"


@pytest.mark.smoke
def test_3(first_entry):
    assert first_entry == "a"


@pytest.mark.regression
def test_4(first_entry):
    assert first_entry > 3


