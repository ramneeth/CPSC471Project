from connection import *
from Person import *

class Client(Person):
    
    def __init__(self,email):
        createClient(email)
        
        
    def getClient(self):
        return self.ssn
        
    def removeC(self, ssn):
        removeClient(ssn)
    