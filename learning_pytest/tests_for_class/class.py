from math import pi


class Circle:
    def __init__(self, radius):
        if type(radius) not in [int, float]:
            raise TypeError('The radius should be int or float')
        if radius < 0:
            raise ValueError('The radius should be positive')
        self.radius = radius

    def get_radius(self):
        return self.radius

    def get_diametr(self):
        return self.radius * 2

    def get_perimetr(self):
        return 2 * pi * self.radius
