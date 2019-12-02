# python -m unittest tests.test_Pencil
import unittest

from src.Pencil import Pencil

class TestCreatePencil(unittest.TestCase):

    def test_no_written_text_to_start(self):
        pencil = Pencil()
        self.assertEqual(pencil.read(), "")

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

    def setUp(self):
        self.pencil = Pencil()
    
    def test_write_oneword(self):
        self.pencil.write("oneword")
        self.assertEqual(self.pencil.read(), "oneword")
        self.assertEqual(self.pencil.pointDurability, 13)

    def test_write_two_words(self):
        self.pencil.write("first")
        self.pencil.write(" second")
        self.assertEqual(self.pencil.read(), "first second")
        self.assertEqual(self.pencil.pointDurability, 9)

    def test_write_beyond_point_durability(self):
        self.pencil.write("There was so much to read for one thing "\
            + "and so much fine health to be pulled down out of the "\
            + "young breath-giving air.")
        expectedText = "There was so much to rea"
        self.assertEqual(self.pencil.read(), expectedText)
        self.assertEqual(self.pencil.pointDurability, 0)

class TestPencilPointDurabilityCost(unittest.TestCase):

    def setUp(self):
        self.pencil = Pencil()

    def test_durability_cost_for_a_lowercase_word(self):
        self.assertEqual(self.pencil.pointDurabilityCost("booger"), 6)

    def test_durability_cost_for_a_uppercase_word(self):
        self.assertEqual(self.pencil.pointDurabilityCost("TABLE"), 10)

    def test_durability_cost_for_whitespace(self):
        self.assertEqual(self.pencil.pointDurabilityCost("\t\n\r   "), 0)

    def test_durability_cost_for_punctuation(self):
        self.assertEqual(self.pencil.pointDurabilityCost("!@#\""), 8)

class TestPencilSharpen(unittest.TestCase):

    def setUp(self):
        self.pencil = Pencil()

    def test_sharpen(self):
        self.pencil.sharpen()
        self.assertEqual(self.pencil.length, 9)
        self.assertEqual(self.pencil.pointDurabilitySharp, self.pencil.pointDurability)

class TestEraser(unittest.TestCase):

    def setUp(self):
        self.pencil = Pencil(pointDurability=50, eraserDurability=20)
        self.pencil.write("There was so much to read for one thing")

    def test_erase_last_word(self):
        self.pencil.erase("thing")
        self.assertEqual(self.pencil.read(), "There was so much to read for one      ")

    def test_erase_middle_phrase(self):
        self.pencil.erase(" so much to read ")
        self.assertEqual(self.pencil.read(), "There was                 for one thing")
    
    def test_erase_first_word(self):
        self.pencil.erase("There")
        self.assertEqual(self.pencil.read(), "      was so much to read for one thing")
    
    def test_erase_word_not_found(self):
        self.pencil.erase("Awesome much")
        self.assertEqual(self.pencil.read(), "There was so much to read for one thing")

    def test_erase_delete_all_o(self):
        self.pencil.erase("o")
        self.pencil.erase("o")
        self.pencil.erase("o")
        self.pencil.erase("o")
        self.assertEqual(self.pencil.read(), "There was s  much t  read f r  ne thing")

class TestEraserDurability(unittest.TestCase):

    def setUp(self):
        self.pencil = Pencil(eraserDurability=3)
        self.pencil.write("Buffalo Bill")

    def test_eraser_runs_out(self):
        self.pencil.erase("Bill")
        self.assertEqual(self.pencil.read(), "Buffalo B   ")

class TestEditing(unittest.TestCase):

    def setUp(self):
        self.pencil = Pencil(pointDurability=50)
        self.pencil.write("An apple a day keeps the doctor away")
        self.pencil.erase("apple")

    def test_edit_one_erased_word_of_same_size(self):
        self.pencil.edit("onion")
        self.assertEqual(self.pencil.read(), "An onion a day keeps the doctor away")
        self.assertEqual(self.pencil.pointDurability, 15)

    def test_edit_one_erased_word_of_larger_size(self):
        self.pencil.edit("artichoke")
        self.assertEqual(self.pencil.read(), "An artich@k@ay keeps the doctor away")