from ConnectionGUI import *
from Person import *

class Admin(Person):
    def __init__(self, database):
        self.ssn = None
        self.fname = None
        self.lname = None
        self.address = None
        self.phone = None
        self.email = None
        self.db == database

    #add a new admin
    def addAdmin(self, email):
        self.db.createAdmin(email)
        self.id = self.db.getAdminID(email)
        self.ssn = self.db.getAdminSSN(email)
        
        
    def removeA(self, email):
        self.db.removeAdmin(email)