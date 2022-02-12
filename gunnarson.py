from xmlrpc.client import Boolean


class Gunnarson:
    '''This is our parachute man class
    
    display()
    '''

    def __init__(self):
        self.man = []
        self.alive = Boolean
        
    def display(self):
        print (self.man)

    def 