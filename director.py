import random
from gunnarson import Gunnarson
from word_selector import WordSelector

class Director:
    '''This class Director will run our main program'''
    
    def __init__(self):

        self._is_playing = True
        self._parachute_man = Gunnarson()
        self._word = WordSelector()
        

   
   
    def __start_game(self):
        '''This will run the basic functions of the game'''
        
    def __word_guess(self):
        '''This will run the guessing portion of the game
        
        It will include three parts:
        1. Get input
        2. Apply Changes
        3. Show Outcomes
        '''
