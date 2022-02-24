
from gunnarson import Gunnarson
from word_selector import WordSelector
from whiteboard import Whiteboard

class Director:
    '''This class Director will run our main program'''
    
    def __init__(self):

        self._is_playing = True
        self._parachute_man = Gunnarson()
        self._word = WordSelector().new_word
        self._whiteboard = Whiteboard(self._word)
        self.letters_guessed = []
        self.alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.guess_successful = True

    def _start_game(self):
        '''This will run the basic functions of the game
        
        '''
        # print(self._word)        # used for testing the new word AND IT WORKS! :D Woohoo! ps, the category is always going to be "fish" for now.
        while self._is_playing:
            self._whiteboard.build_blanks(self.letters_guessed)
            self._parachute_man.display(self.guess_successful,self._whiteboard.completed_word,self.letters_guessed)
            self.still_alive = self._parachute_man.alive
            if not self.still_alive:
                self._is_playing = False
                break
            self.word_completed = self._whiteboard.completed_word
            if self.word_completed == True:
                self._is_playing = False
                break
            self.__letter_guess()
            self.guess_successful = self.update_parachute_man()
        if self.word_completed == True:
            play_again = input(f"Congratulations! You've won! :D\n\nPlay Again? Y/N ").upper()
        else:
            print(f"{self._word}\n")
            play_again = input(f"Game Over.\n\nWould you like to play again? Y/N ").upper()
        if play_again == "Y":
            print("Please close out and open up again. :D thanks for playing!!! C:")
        else:
            print("Thank you, come again any time! Have a great day! :D")


   
    def __letter_guess(self):
        '''This will run the guessing portion of the game
        
        It will include two parts:
        1. Get input
        2. Return it to the right places
        '''
        self.bad_guess = True
        while self.bad_guess:
            self.this_guess = input("Guess a letter: ").lower()
            if self.this_guess in self.letters_guessed:
                print("You already guessed that. Try again, ", end="")
            elif len(list(self.this_guess)) >1:
                print("Only one guess allowed at a time. Try again, ", end="")
            elif self.this_guess not in self.alphabet:
                print("Are you sure that was an English letter? Try again, ", end="")
            else:
                self.letters_guessed.append(self.this_guess)
                self.bad_guess = False

    def update_parachute_man(self):
        if self.this_guess in Whiteboard(self._word).letter_list:
            return True
        else:
            return False
