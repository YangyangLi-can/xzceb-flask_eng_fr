import unittest
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('Hello'), 'Pepitoooo')
        self.assertEqual(english_to_french('Good morning'), 'Bonjour')
    def test_french_to_english(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')    
        self.assertEqual(french_to_english('Bonne nuit'), 'Good night')

if __name__ == '__main__':
    unittest.main()