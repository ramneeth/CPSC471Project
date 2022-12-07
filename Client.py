from Person import *
from ConnectionGUI import *

class Client(Person):
    
    def __init__(self,database):
        self.db = database
        self.email = None
        self.ssn = None
        self.id = None

    def createClient(self,email):
        self.email = email
        results = self.db.createClient(email)
        if(results):
            self.ssn = self.db.getClientID(email)
            self.id = self.db.getClientSSN(email)
        return results
        
    def removeClient(self,email):
        self.email = None
        self.ssn = None
        self.id = None
        results = self.db.removeClient(email)
        return results
        
        
    