import pytest
@pytest.fixture
def fixture_example():
    print("Setup phase")
    yield
    print("Teardown phase")

def test_one(fixture_example):
    print("Inside test")