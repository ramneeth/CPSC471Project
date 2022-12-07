from Person import *

class Client(Person):
    
    def __init__(self,database):
        self.db = database

    def createClient(self,email):
        results = self.db.createClient(email)
        return results
        
    def removeClient(self,email):
        results = self.db.removeClient(email)
        return results
        
    def getClient(self):
        return self.ssn
        
    def removeC(self, ssn):
        removeClient(ssn)
    