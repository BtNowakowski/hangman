from utils import load_words, clear_screen
from random import choice as random_choice
class Hangman:
    def __init__(self, max_guesses:int=12) -> None:
        self.word = None
        self.displayed_word = None
        self.guesses = []
        self.max_guesses = max_guesses
        self.english_words = load_words()
        
    def get_word(self):
        self.word = random_choice(self.english_words).lower()
        self.displayed_word = '_' * len(self.word)
        
    def display_word(self) -> None:
        if self.max_guesses == 0:
            print(f"You lose, the word was: {self.word}")
            exit(0)
        if self.displayed_word == self.word:
            print(f'You win!, the word was: {self.word}')
            exit(0)
        print(f"{self.displayed_word}\n")
        
    def display_user_guesses(self) -> None:
        print(f'You have already guessed for: ', end='')
        for guess in self.guesses:
            print(guess, end=', ')
        print("\n")
        
    def validate_guess(self, guess: str) -> bool:
        if guess.isnumeric():
            clear_screen()
            self.display_user_guesses()
            print('Please enter a letter!')
            return False
        if len(guess) != 1:
            clear_screen()
            self.display_user_guesses()
            print('Please enter a single letter!')
            return False
        if guess in self.guesses:
            clear_screen()
            self.display_user_guesses()
            print('You already guessed that!')
            return False
        return True
            
    def get_guess(self) -> str:
        while True:
            try: 
                guess = input('Guess a letter: ').lower()
            except KeyboardInterrupt:
                print('\nGoodbye!')
                exit(0)
            except ValueError:
                print('Please enter a letter!')
                
            if self.validate_guess(guess):
                break
            continue
        return guess
    
    def check_guess(self, guess: str) -> bool:
        if guess not in self.word:
            self.guesses.append(guess)
            self.max_guesses -= 1
            self.display_user_guesses()
            print(f'Incorrect! You have {self.max_guesses} guesses left.\n')
            return False
        else:
            self.guesses.append(guess)
            self.display_user_guesses()
            print(f'Correct! You have {self.max_guesses} guesses left.\n')
            return True
        
    def update_word(self, guess: str) -> None:
        for i, word in enumerate(self.word):
            for letter in word:
                if letter == guess:
                    self.displayed_word = self.displayed_word[:i] + guess + self.displayed_word[i+1:]

    def main_loop(self) -> None:
        self.get_word()
        while True:
            guess = self.get_guess()
            clear_screen()
            if self.check_guess(guess):
                self.update_word(guess)
            
            self.display_word()
        