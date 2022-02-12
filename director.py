
from gunnarson import Gunnarson
from word_selector import WordSelector
from whiteboard import Whiteboard

class Director:
    '''This class Director will run our main program'''
    
    def __init__(self):

        self._is_playing = True
        self._parachute_man = Gunnarson()
        self._word = WordSelector().new_word
        self._whiteboard = Whiteboard()

    def _start_game(self):
        '''This will run the basic functions of the game
        
        '''
        # print(self._word)               # used for testing the new word AND IT WORKS! :D Woohoo! ps, the category is always going to be "fish" for now.
        while self._is_playing:
            # self._word.display()        # This will likely need to be shown another way so that it does not reveal the word too early. Whiteboard maybe?
            self._parachute_man.display()
            self.__word_guess()
            self.__check_letter()


    # Old we do not have to use, I was just writing what I thought we might do, this was before we met on wednesday, feel free to delete/change as needed:
    # def __word_guess(self):
    #     '''This will run the guessing portion of the game
        
    #     It will include three parts:
    #     1. Get input
    #     2. Apply Changes
    #     3. Show Outcomes
    #     '''

