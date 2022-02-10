
from gunnarson import Gunnarson
from word_selector import WordSelector
from whiteboard import Whiteboard

class Director:
    '''This class Director will run our main program'''
    
    def __init__(self):

        self._is_playing = True
        self._parachute_man = Gunnarson()
        self._word = WordSelector()
        self.whiteboard = Whiteboard()

    def __start_game(self):
        '''This will run the basic functions of the game
        
        '''
        while self._is_playing:
           # self._word.display()
            self._parachute_man.display()
            self.__word_guess()
            self.__check_letter()


        
    def __word_guess(self):
        '''This will run the guessing portion of the game
        
        It will include three parts:
        1. Get input
        2. Apply Changes
        3. Show Outcomes
        '''

