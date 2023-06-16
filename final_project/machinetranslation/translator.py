"""
This module provides functions for translating text between English and French.
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translates a given English text to French using the MyMemoryTranslator API.

    Args:
        englishText: A string representing the English text to be translated.

    Returns:
        A string representing the translated French text.
    """
    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    return french_text.strip()

def french_to_english(french_text):
    """
    Translates a given French text to English using the MyMemoryTranslator API.

    Args:
        frenchText: A string representing the French text to be translated.

    Returns:
        A string representing the translated English text.
    """
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    return english_text.strip()
