from connection import *
from Person import *

class Admin(Person):
    def __init__(self, datbase):
        self.ssn = None
        self.fname = None
        self.lname = None
        self.address = None
        self.phone = None
        self.email = None
        
    
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
        createAdmin(ssn, email, phone, f, l, address)
        self.id = getAdminID(ssn)
        
        
    def removeA(self, email):
        removeAdmin(email)