'''
Module for language translation
'''
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    #write the code here
    '''Method to translate EN -> FR'''
    french_text = MyMemoryTranslator(source='english', target= 'french').translate(english_text)
    return french_text

def french_to_english(french_text):
    #write the code here
    '''Method to translate FR -> EN'''
    english_text = MyMemoryTranslator(source='french', target= 'english').translate(french_text)
    return english_text
    