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
        
    
    #get the ssn for the admin
    def getAdmin(self):
        return self.ssn

    #add a new 
    def addAdmin(self, ssn, email, phone, f, l, address):
        self.ssn = ssn
        self.email = email
        self.phone = phone
        self.fname = f
        self.lname = l
        self.address = address
        self.db.createAdmin(ssn, email, phone, f, l, address)
        self.id = self.db.getAdminID(ssn)
        
        
    def removeA(self, email):
        self.db.removeAdmin(email)