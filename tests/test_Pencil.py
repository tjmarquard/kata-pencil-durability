import unittest

from src.Pencil import Pencil

# python -m unittest tests.test_Pencil.TestPencilWrite
class TestPencilWrite(unittest.TestCase):
    
    def test_write_oneword(self):
        pencil = Pencil()
        pencil.write("oneword")
        self.assertEqual(pencil.writtenText, "oneword")
        self.assertEqual(pencil.pointDurability, 13)

    def test_write_two_words(self):
        pencil = Pencil()
        pencil.write("first")
        pencil.write(" second")
        self.assertEqual(pencil.writtenText, "first second")
        self.assertEqual(pencil.pointDurability, 9)

    def test_set_default_point_durability(self):
        pencil = Pencil()
        self.assertEqual(pencil.pointDurability, 20)

    def test_write_beyond_point_durability(self):
        pencil = Pencil()
        pencil.write("There was so much to read for one thing "\
            + "and so much fine health to be pulled down out of the "\
            + "young breath-giving air.")
        expectedText = "There was so much to rea"
        self.assertEqual(pencil.writtenText, expectedText)
        self.assertEqual(pencil.pointDurability, 0)

# python -m unittest tests.test_Pencil.TestPencilTextDurabilityCost
class TestPencilTextDurabilityCost(unittest.TestCase):

    def test_durability_cost_for_a_lowercase_word(self):
        pencil = Pencil()
        self.assertEqual(pencil.textDurabilityCost("booger"), 6)

    def test_durability_cost_for_a_uppercase_word(self):
        pencil = Pencil()
        self.assertEqual(pencil.textDurabilityCost("TABLE"), 10)

    def test_durability_cost_for_whitespace(self):
        pencil = Pencil()
        self.assertEqual(pencil.textDurabilityCost("\t\n\r   "), 0)

    def test_durability_cost_for_punctuation(self):
        pencil = Pencil()
        self.assertEqual(pencil.textDurabilityCost("!@#\""), 8)

class TestPencilSharpen(unittest.TestCase):

    def test_sharpen(self):
        pencil = Pencil()
        self.assertEqual(pencil.sharpen(), 9)