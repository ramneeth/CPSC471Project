from connection import *
from Person import *

class Admin(Person):
    def __init__(self, ssn, email, phone, f, l, address):
        self.ssn = ssn
        self.fname = f
        self.lname = l
        self.address = address
        self.phone = phone
        self.email = email
        createAdmin(ssn, email, phone, f, l, address)
        self.id = getAdminID(ssn)
    
    #get the ssn for the admin
    def getAdmin(self):
        return self.ssn

    #add a new 
    def addAdmin(self, person):
        addNewAdmin(person.ssn, person.fname, person.lname, person.address,
                    person.phone, person.email, self.id)
        self.id = getAdminID(person.ssn)
        
    def removeA(self, ssn):
        removeAdmin(ssn)