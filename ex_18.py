import string

def is_pangram(sentence):
    english_alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for c in english_alphabet:
        if c not in sentence.lower():
            return False   
    return True
    