from os import name, system
def load_words():
    with open('assets/english_words.txt') as word_file:
        valid_words = list(set(word_file.read().split()))
    return valid_words
def clear_screen():
    if name == 'nt':
        system('cls')
    else:
        system('clear')
    
