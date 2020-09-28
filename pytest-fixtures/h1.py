import pytest

@pytest.fixture(scope='session')
def fixture_sess():
    yield
    # tearing down fixtures
    print("Session fixture complete")

@pytest.fixture(scope="module")
def fixture_modl():
    yield
    print("Module fixture complete")

@pytest.fixture(scope='class')
def fixture_clss():
    yield
    print("Class fixture complete")

@pytest.fixture(scope='function')
def fixture_func():
    yield
    print("Function fixture complete")

class TestClass:
    @pytest.mark.usefixtures('fixture_sess', 'fixture_modl', 'fixture_clss', 'fixture_func')
    def test_one(self):
        print("Inside test")
