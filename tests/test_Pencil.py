import unittest

from src.Pencil import Pencil

# python -m unittest tests.test_Pencil.TestPencil
class TestPencil(unittest.TestCase):
    
    def test_write_oneword(self):
        pencil = Pencil()
        Pencil.write(pencil, "oneword")
        self.assertEqual(pencil.writtenText, "oneword")

    def test_write_two_words(self):
        pencil = Pencil()
        Pencil.write(pencil, "first")
        Pencil.write(pencil, " second")
        self.assertEqual(pencil.writtenText, "first second")