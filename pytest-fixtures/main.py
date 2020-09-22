import pytest

@pytest.fixture(scope='session')
def fixture_session():
    print("Inside fixture session")

@pytest.fixture(scope="module")
def fixture_module():
    print("Inside fixture mudule")

@pytest.fixture(scope='class')
def ficture_class():
    print("Inside fixture class")

@pytest.fixture(scope='function')
def fixture_function():
    print("Inside fixture function")

class TestOrder:
    @pytest.mark.usefixtures('fixture_session', 'fixture_module', 'fixture_class', 'fixture_function')
    def test_one(self):
        print("Inside test")