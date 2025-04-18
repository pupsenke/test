import unittest
from testapp import is_equilateral

class TestEquilateralTriangle(unittest.TestCase):
    def test_all_sides_equal(self):
        self.assertTrue(is_equilateral(5, 5, 5))
        self.assertTrue(is_equilateral(0.1, 0.1, 0.1))
    
    def test_two_sides_equal(self):
        self.assertFalse(is_equilateral(5, 5, 3))
        self.assertFalse(is_equilateral(2, 3, 2))
    
    def test_all_sides_different(self):
        self.assertFalse(is_equilateral(3, 4, 5))
    
    def test_zero_or_negative_sides(self):
        # Функция не проверяет валидность треугольника, но можно проверить поведение
        self.assertFalse(is_equilateral(0, 0, 0))
        self.assertFalse(is_equilateral(-1, -1, -1))
        self.assertFalse(is_equilateral(-1, 1, 1))

if __name__ == '__main__':
    unittest.main()
