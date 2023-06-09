import unittest
from translator import english_to_french, french_to_english

class TranslationTests(unittest.TestCase):
    def test_english_to_french(self):
        """
        Translate English text to French.
        """
        english_text = "Hello"
        expected_french_text = "Pepitoooo"
        translated_text = english_to_french(english_text)
        self.assertEqual(translated_text, expected_french_text)

    def test_english_to_french_2(self):
        """
        Translate English text to French.
        """
        english_text = "Bye"
        expected_french_text = "Au revoir"
        translated_text = english_to_french(english_text)
        self.assertEqual(translated_text, expected_french_text)

    def test_french_to_english(self):
        """
        Translate French text to English.
        """
        french_text = "Bonjour"
        expected_english_text = "Hello"
        translated_text = french_to_english(french_text)
        self.assertEqual(translated_text, expected_english_text)

    def test_french_to_english_2(self):
        """
        Translate French text to English.
        """
        french_text = "Au revoir"
        expected_english_text = "Goodbye"
        translated_text = french_to_english(french_text)
        self.assertEqual(translated_text, expected_english_text)

if __name__ == '__main__':
    unittest.main()
