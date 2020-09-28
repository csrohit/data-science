import pytest
@pytest.mark.parametrize("val, out",[(3, 27),
(4, 15),
(5, 125)])
def test_square(val, out):
    print("val^3:", val**3)
    assert val**3 == out
