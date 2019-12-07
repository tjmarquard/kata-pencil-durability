import unittest
from unittest.mock import patch

from src.pencil import *

class TestCreatePencil(unittest.TestCase):

    def test_no_written_text_to_start(self):
        pencil = Pencil()
        self.assertEqual(pencil.read(), "")

    def test_set_point_durability_when_sharp(self):
        pencil = Pencil()
        self.assertEqual(pencil.point_durability, 20)
        self.assertEqual(pencil.point_durability_sharp, 20)
    
    def test_set_point_durability_when_sharp_40(self):
        pencil = Pencil(point_durability=40)
        self.assertEqual(pencil.point_durability, 40)
        self.assertEqual(pencil.point_durability_sharp, 40)

    def test_set_pencil_length(self):
        pencil = Pencil()
        self.assertEqual(pencil.length, 10)

    def test_set_pencil_length_5(self):
        pencil = Pencil(length=5)
        self.assertEqual(pencil.length, 5)

    def test_set_eraser_durability(self):
        pencil = Pencil()
        self.assertEqual(pencil.eraser_durability, 10)

    def test_set_eraser_durability_20(self):
        pencil = Pencil(eraser_durability=20)
        self.assertEqual(pencil.eraser_durability, 20)

class TestPencilWrite(unittest.TestCase):

    def setUp(self):
        self.pencil = Pencil()
    
    def test_write_oneword(self):
        self.pencil.write("oneword")
        self.assertEqual(self.pencil.read(), "oneword")
        self.assertEqual(self.pencil.point_durability, 13)

    def test_write_two_words(self):
        self.pencil.write("first")
        self.pencil.write(" second")
        self.assertEqual(self.pencil.read(), "first second")
        self.assertEqual(self.pencil.point_durability, 9)

    def test_write_beyond_point_durability(self):
        self.pencil.write("There was so much to read for one thing "\
            + "and so much fine health to be pulled down out of the "\
            + "young breath-giving air.")
        expectedText = "There was so much to rea"
        self.assertEqual(self.pencil.read(), expectedText)
        self.assertEqual(self.pencil.point_durability, 0)

class TestPencilPointDurabilityCost(unittest.TestCase):

    def setUp(self):
        self.pencil = Pencil()

    def test_durability_cost_for_a_lowercase_word(self):
        self.assertEqual(self.pencil.point_durability_cost("booger"), 6)

    def test_durability_cost_for_a_uppercase_word(self):
        self.assertEqual(self.pencil.point_durability_cost("TABLE"), 10)

    def test_durability_cost_for_whitespace(self):
        self.assertEqual(self.pencil.point_durability_cost("\t\n\r   "), 0)

    def test_durability_cost_for_punctuation(self):
        self.assertEqual(self.pencil.point_durability_cost("!@#\""), 8)

class TestPencilSharpen(unittest.TestCase):

    def setUp(self):
        self.pencil = Pencil()

    def test_sharpen(self):
        self.pencil.sharpen()
        self.assertEqual(self.pencil.length, 9)
        self.assertEqual(self.pencil.point_durability_sharp, 
                         self.pencil.point_durability)

class TestEraser(unittest.TestCase):

    def setUp(self):
        self.pencil = Pencil(point_durability=50, eraser_durability=20)
        self.pencil.write("There was so much to read for one thing")

    def test_erase_last_word(self):
        self.pencil.erase("thing")
        self.assertEqual(self.pencil.read(), 
                         "There was so much to read for one      ")

    def test_erase_middle_phrase(self):
        self.pencil.erase(" so much to read ")
        self.assertEqual(self.pencil.read(),
                         "There was                 for one thing")
    
    def test_erase_first_word(self):
        self.pencil.erase("There")
        self.assertEqual(self.pencil.read(), 
                         "      was so much to read for one thing")
    
    def test_erase_word_not_found(self):
        self.pencil.erase("Awesome much")
        self.assertEqual(self.pencil.read(), 
                         "There was so much to read for one thing")

    def test_erase_delete_all_o(self):
        self.pencil.erase("o")
        self.pencil.erase("o")
        self.pencil.erase("o")
        self.pencil.erase("o")
        self.assertEqual(self.pencil.read(), 
                         "There was s  much t  read f r  ne thing")

class TestEraserDurability(unittest.TestCase):

    def setUp(self):
        self.pencil = Pencil(eraser_durability=3)
        self.pencil.write("Buffalo Bill")

    def test_eraser_runs_out(self):
        self.pencil.erase("Bill")
        self.assertEqual(self.pencil.read(), "Buffalo B   ")

class TestEditing(unittest.TestCase):

    def setUp(self):
        self.pencil = Pencil(point_durability=50)
        self.pencil.write("An apple a day keeps the doctor away")
        self.pencil.erase("apple")

    def test_edit_one_erased_word_of_same_size(self):
        self.pencil.edit("onion")
        self.assertEqual(self.pencil.read(), 
                         "An onion a day keeps the doctor away")
        self.assertEqual(self.pencil.point_durability, 15)

    def test_edit_two_words_when_only_one_erased(self):
        self.pencil.edit("onion")
        self.pencil.edit("peach")
        self.assertEqual(self.pencil.read(), 
                         "An onion a day keeps the doctor away")
        self.assertEqual(self.pencil.point_durability, 15)

    def test_edit_one_erased_word_of_larger_size(self):
        self.pencil.edit("artichoke")
        self.assertEqual(self.pencil.read(), 
                         "An artich@k@ay keeps the doctor away")

class TestBuildPencil(unittest.TestCase):
  
    @patch('src.pencil.input_length')
    @patch('src.pencil.input_eraser_durability')
    @patch('src.pencil.input_point_durability')
    def test_build_pencil(self,
                          mock_point_durability,
                          mock_eraser_durability,
                          mock_length):
        mock_point_durability.return_value = 100
        mock_eraser_durability.return_value = 200
        mock_length.return_value = 300
        pencil = build_pencil()
        self.assertEqual(pencil.point_durability, 100)
        self.assertEqual(pencil.eraser_durability, 200)
        self.assertEqual(pencil.length, 300)

    @patch('builtins.input')
    def test_point_durability_input(self, mock_input):
        mock_input.return_value = "200"
        point_durability = input_point_durability()
        self.assertEqual(point_durability, 200)
        self.assertIsInstance(point_durability, int)
    
    @patch('builtins.input')
    def test_point_eraser_input(self, mock_input):
        mock_input.return_value = "200"
        eraser_durability = input_eraser_durability()
        self.assertEqual(eraser_durability, 200)
        self.assertIsInstance(eraser_durability, int)
    
    @patch('builtins.input')
    def test_length_input(self, mock_input):
        mock_input.return_value = "200"
        length = input_length()
        self.assertEqual(length, 200)
        self.assertIsInstance(length, int)

    @patch('builtins.input')
    def test_attribute_input(self, expected_value):
        expected_value.return_value = "200"
        attribute_value = input_attribute("prompt text")
        self.assertEqual(attribute_value, 200)

    def test_massage_input(self):
        massaged_value = massage_input("200")
        self.assertEqual(massaged_value, 200)
        self.assertIsInstance(massaged_value, int)
    
    def test_massage_input_blank(self):
        massaged_value = massage_input("")
        self.assertEqual(massaged_value, "")
        self.assertIsInstance(massaged_value, str)
    
    def test_massage_input_negative(self):
        massaged_value = massage_input("-50")
        self.assertEqual(massaged_value, "")
        self.assertIsInstance(massaged_value, str)