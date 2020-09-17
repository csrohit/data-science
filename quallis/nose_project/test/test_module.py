from proj.circle import Circle
from nose.tools import assert_raises, assert_equals

class TestingCircleCreation:
    def test_creating_circle_with_numeric_radius(self):
        c1 = Circle(2.5)
        assert_equals(c1.radius, 2.5)

    def test_creating_circle_with_negative_radius(self):
        with assert_raises(ValueError) as error:
            c1 = Circle(-2.5)
            assert_equals("radius must be between 0 and 1000 inclusive" in error)

    def test_creating_circle_with_greaterthan_radius(self):
        with assert_raises(ValueError) as error:
            c1 = Circle(1000.1)
            assert_equals("radius must be between 0 and 1000 inclusive" in error)
    def test_creating_circle_with_nonnumeric_radius(self):
        with assert_raises(TypeError) as error:
            c1 = Circle('hello')
            assert_equals("radius must be between 0 and 1000 inclusive" in error)

class TestCircleArea:
    def test_circlearea_with_random_numeric_radius(self):
        c1 = Circle(2.5)
        assert_equals(c1.area(), 19.63)
    def test_circlearea_with_min_radius(self):
        c1 = Circle(0)
        assert_equals(c1.area(), 0)
    def test_circlearea_with_max_radius(self):
        c1 = Circle(1000)
        assert_equals(c1.area(), 3141592.65)

class TestCircleCircumference:
    def test_circlecircum_with_random_numeric_radius(self):
        c1 = Circle(2.5)
        assert_equals(c1.circumference(), 15.71)
    def test_circlecircum_with_min_radius(self):
        c1 = Circle(0)
        assert_equals(c1.circumference(), 0)
    def test_circlecircum_with_max_radius(self):
        c1 = Circle(1000)
        assert_equals(c1.circumference(), 6283.19)

