# from posixpath import split
# from shutil import which
# from word_selector import WordSelector


class Whiteboard:

    '''This is our whiteboard for the blank spaces to be filled out
    
    '''
    def __init__(self,word):
        self.word = word
        self.letter_list = list(self.word)
        self.numOfLetters = len(self.letter_list)
        self.output_blanks_and_letters = []
        self.completed_word = False
        

    def build_blanks(self,letters_guessed=[]):
        self.letters_guessed = letters_guessed
        self.output_blanks_and_letters.clear()
        for i in range(self.numOfLetters):
            self.output_blanks_and_letters.append("_")
            if self.letter_list[i] == " ":
                self.output_blanks_and_letters[i] = " "
            elif self.letter_list[i] == "-":
                self.output_blanks_and_letters[i] = "-"
            elif self.letter_list[i] in self.letters_guessed:
                self.output_blanks_and_letters[i] = self.letter_list[i]
            else:
                self.output_blanks_and_letters[i] = "_"
        for i in range(len(self.output_blanks_and_letters)):
            print(self.output_blanks_and_letters[i], end=" ")
        print("")
        if "_" not in self.output_blanks_and_letters:
            self.completed_word = True


    def check_letter(self):

        self.numOfLetters = len(self.word.new_word)
        
        print(self.word.new_word)
        print(len(self.word.new_word))

    def replacing(self):
       pass
