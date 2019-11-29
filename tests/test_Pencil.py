import unittest

from src.Pencil import Pencil

# python -m unittest tests.test_Pencil.TestPencil
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
