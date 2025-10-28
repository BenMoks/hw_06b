import unittest
from Triangle import classifyTriangle

class TestTriangles(unittest.TestCase):
    def test_equilateral_integers(self):
        self.assertEqual(classifyTriangle(3, 3, 3), "Equilateral")

    def test_isosceles_integers(self):
        self.assertEqual(classifyTriangle(5, 5, 8), "Isosceles")
        self.assertEqual(classifyTriangle(5, 8, 5), "Isosceles")
        self.assertEqual(classifyTriangle(8, 5, 5), "Isosceles")

    def test_scalene_integers(self):
        self.assertEqual(classifyTriangle(4, 5, 6), "Scalene")

    def test_right_triangles(self):
        self.assertEqual(classifyTriangle(3, 4, 5), "Right")
        self.assertEqual(classifyTriangle(5, 12, 13), "Right")
        self.assertEqual(classifyTriangle(6, 8, 10), "Right")

    def test_permutation_insensitive(self):
        self.assertEqual(classifyTriangle(4, 5, 6), classifyTriangle(6, 5, 4))
        self.assertEqual(classifyTriangle(3, 4, 5), classifyTriangle(5, 4, 3))

    def test_zeros_and_negatives(self):
        self.assertEqual(classifyTriangle(0, 1, 1), "InvalidInput")
        self.assertEqual(classifyTriangle(-1, 2, 2), "InvalidInput")

    def test_triangle_inequality_violations(self):
        self.assertEqual(classifyTriangle(1, 2, 3), "NotATriangle")
        self.assertEqual(classifyTriangle(1, 3, 2), "NotATriangle")
        self.assertEqual(classifyTriangle(3, 1, 2), "NotATriangle")
        self.assertEqual(classifyTriangle(2, 2, 5), "NotATriangle")

    def test_non_integer_types(self):
        self.assertEqual(classifyTriangle(3.0, 4, 5), "InvalidInput")
        self.assertEqual(classifyTriangle("3", 4, 5), "InvalidInput")

    def test_extreme_values(self):
        self.assertEqual(classifyTriangle(200, 201, 401), "NotATriangle")
        self.assertEqual(classifyTriangle(200, 201, 300), "Scalene")

if __name__ == "__main__":
    unittest.main()
