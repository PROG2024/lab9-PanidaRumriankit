"""Unit tests of the Circle class using unittest or pytest (your choice).

Write unit tests as described in README.md.

1. Unit test for add_area using typical values.
2. Unit test for add_area for an "edge case" where one circle has radius 0.
3. Unit test that circle constructor raises exception of radius is negative.

"""
import math

from circle import Circle
import unittest
# TODO write 3 tests as described above


class CircleTest(unittest.TestCase):
    def setUp(self) -> None:
        self.circle1 = Circle(2)
        self.circle2 = Circle(0)
        self.circle4 = Circle(4)

    def test_typical_case(self):
        r1 = self.circle1.get_radius()
        r2 = self.circle4.get_radius()
        r = math.hypot(r1, r2)
        self.assertEqual(r, Circle.add_area(self.circle1, self.circle4).radius)

    def test_edge_case(self):
        self.assertEqual(Circle.add_area(self.circle2, self.circle4).radius, Circle.add_area(self.circle4, self.circle2).radius)

    def test_error_less0(self):
        with self.assertRaises(ValueError):
            self.circle3 = Circle(-2)
