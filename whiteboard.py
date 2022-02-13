from posixpath import split
from shutil import which
from word_selector import WordSelector

class Whiteboard:

    '''This is our whiteboard for the blank spaces to be filled out
    
    '''
    def __init__(self):
        self.word = WordSelector()
        self.numOfLetters = 0
        self.userGuess = ""
        self.__self.blanks = ""

    def check_letter(self):

        self.numOfLetters = len(self.word.new_word)
        
        print(self.word.new_word)
        print(len(self.word.new_word))

    def replacing(self):
       pass