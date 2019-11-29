import unittest

from src.Pencil import Pencil

# python -m unittest tests.test_Pencil.TestPencilWrite
class TestPencilWrite(unittest.TestCase):
    
    def test_write_oneword(self):
        pencil = Pencil()
        pencil.write("oneword")
        self.assertEqual(pencil.writtenText, "oneword")

    def test_write_two_words(self):
        pencil = Pencil()
        pencil.write("first")
        pencil.write(" second")
        self.assertEqual(pencil.writtenText, "first second")

    def test_set_default_point_durability(self):
        pencil = Pencil()
        self.assertEqual(pencil.pointDurability, 20)

# python -m unittest tests.test_Pencil.TestPencilDegradePoint
class TestPencilDegradePoint(unittest.TestCase):

    def test_points_left_to_write_after_writing_a_lowercase_word(self):
        pencil = Pencil()
        pencil.degradePoint("booger")
        self.assertEqual(pencil.pointDurability, 14)