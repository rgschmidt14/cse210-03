from xmlrpc.client import Boolean


class Gunnarson:
    '''This is our parachute man class
    
    display()
    '''

    def __init__(self):
        self.parachute = {}
        self.parachute[1] = "   ___\n"
        self.parachute[2] = "  /___\ \n"
        self.parachute[3] = "  \   /\n"
        self.parachute[4] = "   \ /     "
        self.man = {
            "alive":["\n    O","  '-|-' ","   / \ ","","^^^^^^^^^^^"], 
            "dead":["   x","  /|\ ","   \\\\ ","^^^^^^^^^^^"]
        }
        self.alive = True
        self.__counter = 0
        
    def display(self,successful_guess,word_completed,letters_guessed):
        
        # print (self.parachute["line1"])
        # print (self.parachute["line2"])
        # print (self.parachute["line3"])
        # print (self.parachute["line4"])
        if not successful_guess:
            self.cutLine()
            
        if word_completed:
            del self.man["alive"][3]
            for item in self.parachute:
                print(self.parachute[item])
            for i in range(len(self.man["alive"])):
                print (self.man["alive"][i])
        elif self.alive == False:
            for i in range(len(self.man["dead"])):
                print (self.man["dead"][i])
        else:
            for item in self.parachute:
                print(self.parachute[item], end="")
            for letter in letters_guessed:
                print(letter, end=" ")
            for i in range(len(self.man["alive"])):
                print (self.man["alive"][i])

    
        
    def cutLine(self):
        self.__counter += 1
        if self.__counter < 5:
            del self.parachute[self.__counter]
        else:
            self.alive = False
        

