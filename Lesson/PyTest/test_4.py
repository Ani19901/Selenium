import pytest


@pytest.mark.parametrize("x, y, z", [(1,2,3), (4,5,6),(7,8,9),(1,2,3)])
def test_5(x, y, z):
    assert x * y + z == 5


