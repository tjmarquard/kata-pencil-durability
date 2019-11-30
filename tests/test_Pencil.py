# python -m unittest tests.test_Pencil
import unittest

from src.Pencil import Pencil

class TestCreatePencil(unittest.TestCase):

    def test_no_written_text_to_start(self):
        pencil = Pencil()
        self.assertEqual(pencil.writtenText, "")

    def test_set_point_durability_when_sharp(self):
        pencil = Pencil()
        self.assertEqual(pencil.pointDurability, 20)
        self.assertEqual(pencil.pointDurabilitySharp, 20)
    
    def test_set_point_durability_when_sharp_40(self):
        pencil = Pencil(pointDurability=40)
        self.assertEqual(pencil.pointDurability, 40)
        self.assertEqual(pencil.pointDurabilitySharp, 40)

    def test_set_pencil_length(self):
        pencil = Pencil()
        self.assertEqual(pencil.length, 10)

    def test_set_pencil_length_5(self):
        pencil = Pencil(length=5)
        self.assertEqual(pencil.length, 5)

    def test_set_eraser_durability(self):
        pencil = Pencil()
        self.assertEqual(pencil.eraserDurability, 10)

    def test_set_eraser_durability_20(self):
        pencil = Pencil(eraserDurability=20)
        self.assertEqual(pencil.eraserDurability, 20)

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

    def test_write_beyond_point_durability(self):
        pencil = Pencil()
        pencil.write("There was so much to read for one thing "\
            + "and so much fine health to be pulled down out of the "\
            + "young breath-giving air.")
        expectedText = "There was so much to rea"
        self.assertEqual(pencil.writtenText, expectedText)
        self.assertEqual(pencil.pointDurability, 0)

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
        pencil.write("booger")
        pencil.sharpen()
        self.assertEqual(pencil.length, 9)
        self.assertEqual(pencil.pointDurabilitySharp, pencil.pointDurability)

class TestEraser(unittest.TestCase):

    def test_erase_last_word(self):
        pencil = Pencil(pointDurability=50)
        pencil.write("There was so much to read for one thing")
        pencil.erase("thing")
        self.assertEqual(pencil.writtenText, "There was so much to read for one      ")

    def test_erase_middle_phrase(self):
        pencil = Pencil(pointDurability=50)
        pencil.write("There was so much to read for one thing")
        pencil.erase(" so much to read ")
        self.assertEqual(pencil.writtenText, "There was                 for one thing")
    
    def test_erase_first_word(self):
        pencil = Pencil(pointDurability=50)
        pencil.write("There was so much to read for one thing")
        pencil.erase("There")
        self.assertEqual(pencil.writtenText, "      was so much to read for one thing")
    
    def test_erase_word_not_found(self):
        pencil = Pencil(pointDurability=50)
        pencil.write("There was so much to read for one thing")
        pencil.erase("Awesome much")
        self.assertEqual(pencil.writtenText, "There was so much to read for one thing")

    def test_erase_delete_all_o(self):
        pencil = Pencil(pointDurability=50)
        pencil.write("There was so much to read for one thing")
        pencil.erase("o")
        pencil.erase("o")
        pencil.erase("o")
        pencil.erase("o")
        self.assertEqual(pencil.writtenText, "There was s  much t  read f r  ne thing")
        