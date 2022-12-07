from ConnectionGUI import *
from Person import *

class RestrictedUser(Person):
    def __init__(self, database):
        self.ssn = None
        self.id = None
        self.email = None
        
        self.db = database
        
    def addUser(self, email):
        self.email = email
        self.db.createRUser(email)
        self.id = self.db.getRUserID(email)
        self.ssn = self.db.getRUserSSN(email)
        