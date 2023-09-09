from os import name, system

ASCII_HANGMAN = {
    8: """
  +---+
      |
      |
      |
      |
      |
=========""",
    7: """
  +---+
      |
  O   |
      |
      |
      |
=========""",
    6: """
  +---+
      |
  O   |
  |   |
      |
      |
=========""",
    5: """
  +---+
      |
  O   |
 /|   |
      |
      |
=========""",
    4: """
  +---+
      |
  O   |
 /|\  |
      |
      |
=========""",
    3: """
  +---+
      |
  O   |
 /|\  |
 /    |
      |
=========""",
    2: """
  +---+
      |
  O   |
 /|\  |
 / \  |
      |
=========""",
    1: """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========""",
}


def load_words():
    with open("assets/english_words.txt") as word_file:
        valid_words = list(set(word_file.read().split()))
    return valid_words


def clear_screen():
    if name == "nt":
        system("cls")
    else:
        system("clear")


def get_ascii_hangman(round):
    print(ASCII_HANGMAN[round])
