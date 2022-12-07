from ConnectionGUI import *
from Employee import *

class Associate(Employee):
    def __init__(self, database):
        self.ssn = None
        self.id = None
        self.email = None
        self.db = database
        
        
    def addAssociate(self, email):
        self.email = email
        self.db.createAssociate(email)
        self.id = self.db.getAssociateID(email)
        self.ssn = self.db.getAssociateSSN(email)
    
