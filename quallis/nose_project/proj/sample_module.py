import math
class Circle:

    def __init__(self, radius):
        # Define initialization method:
        if not (isinstance(radius, int) or isinstance(radius, float)):
            raise TypeError("radius must be a number")
        elif not (radius >= 0 and radius <= 1000):
            raise ValueError("radius must be between 0 and 1000 inclusive")
        else:
            self.radius = radius

    def area(self):
        # Define area functionality:
        return round(math.pi * (self.radius ** 2),2)

    def circumference(self):
        # Define circumference functionality:
        return round(2 * math.pi * self.radius, 2)
