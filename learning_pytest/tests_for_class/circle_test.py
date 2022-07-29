import pytest
from circle_class import Circle

class TestCircle:
    def test_get_radius(self):
        circle = Circle(1)
        assert circle.get_radius() == 1, 'error in radius'

    def test_get_diameter(self):
        circle = Circle(1)
        assert circle.get_diameter() == 2, 'error in diameter'

    def test_get_perimeter(self):
        circle = Circle(1)
        assert round(circle.get_perimeter(), 2) == 6.28, 'error in perimeter'

    def test_init_type_error(self):
        with pytest.raises(TypeError):
            circle = Circle('1')

    def test_init_value_error(self):
        with pytest.raises(ValueError):
            circle = Circle(-1)
