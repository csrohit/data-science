import pytest
@pytest.fixture
def create_student():
    def _create_student(name):
        return {
            'name': name,
            'grade': 'A'
        }
    return _create_student

def test_one(create_student):
    o1 = create_student("Ravi")
    o2 = create_student("Abdul")
    print(o1)
    print(o2)
