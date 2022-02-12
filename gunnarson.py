from xmlrpc.client import Boolean


class Gunnarson:
    '''This is our parachute man class
    
    display()
    '''

    def __init__(self):
        self.parachute = {}
        self.man = {}
        self.alive = Boolean
        
    def display(self):
        self.parachute["line1"] = " ___"
        self.parachute["line2"] = "/___\ "
        self.parachute["line3"] = "\   /"
        self.parachute["line4"] = " \ /"
        print (self.parachute["line1"])
        print (self.parachute["line2"])
        print (self.parachute["line3"])
        print (self.parachute["line4"])
        
    def cutLine(self):
        for i in self.parachute:
            del self.parachute[i]
            print (self.parachute)
        

trying = Gunnarson()
trying.display()

