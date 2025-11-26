"""
Simple tests
"""

import unittest

from functions import create_canvas, draw_line, check_email, rotate_x, rotate_y, rotate_z


class TestCanvas(unittest.TestCase):
    def test_create_canvas(self):
        canvas = create_canvas(10, 5)
        self.assertEqual(len(canvas), 5)
        self.assertEqual(len(canvas[0]), 10)

    def test_draw_line(self):
        canvas = create_canvas(10, 10)
        draw_line(canvas, 1, 1, 5, 5)
        self.assertNotEqual(canvas[1][1], ' ')
        self.assertNotEqual(canvas[5][5], ' ')


class TestRotations(unittest.TestCase):
    def test_rotate_x(self):
        result = rotate_x([1, 0, 0], 0)
        self.assertEqual(len(result), 3)

    def test_rotate_y(self):
        result = rotate_y([0, 1, 0], 0)
        self.assertEqual(len(result), 3)

    def test_rotate_z(self):
        result = rotate_z([0, 0, 1], 0)
        self.assertEqual(len(result), 3)


class TestEmailValidation(unittest.TestCase):
    def test_valid_email(self):
        self.assertTrue(check_email("user@example.com"))

    def test_invalid_email(self):
        self.assertFalse(check_email("userexample.com"))

    def test_invalid_email_no_domain(self):
        self.assertFalse(check_email("user@"))

    def test_invalid_email_empty(self):
        self.assertFalse(check_email(""))


if __name__ == '__main__':
    unittest.main()



