import unittest

from src.Pencil import Pencil

# python -m unittest tests.test_Pencil.TestPencil
class TestPencil(unittest.TestCase):
    
    def test_write_oneword(self):
        self.assertEqual(Pencil.write(self, "oneword"), "oneword")