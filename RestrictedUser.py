from connection import *
from Person import *

class RestrictedUser(Person):
    def __init__(self, database):
        self.ssn = None
        self.fname = None
        self.lname = None
        self.address = None
        self.phone = None
        self.email = None
        self.password = None
        self.db = database
        
    def addUser(self, ssn, email, phone, f, l, address, password):
        self.ssn = ssn
        self.fname = f
        self.lname = l
        self.address = address
        self.phone = phone
        self.email = email
        self.password = password
        createRUser(ssn, id, email, phone, f, l, address, password)
        self.id = getRUserID(ssn)
        
    def getRUser(self):
        return self.ssn

    def addRUser(self, person):
        self.id = getRUserID(self.ssn)
        addNewUser(person.ssn, person.fname, person.lname, person.address,
                    person.phone, person.email, self.id, person.password)
        
    def removeRU(self, ssn):
        removeRUser(ssn)
        