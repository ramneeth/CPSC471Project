from connection import *
from Admin import *

class Owner(Admin):
    def __init__(self):
        self.ssn = 123456789
        self.fname = "Jalal"
        self.lname = "Kawash"
        self.address = "2500 University Dr NW, Calgary, AB T2N 1N4"
        self.phone = 4034034033
        self.email = "jalal.kawash@ucalgary.ca"
        self.password = "cpsc"
        createPerson(self.ssn, self.fname, self.lname, self.address, self.phone, self.email, self.password)
        createOwner(self.ssn, self.email, self.phone, self.fname, self.lname, self.address, self.password)
        self.id = getOwnerID(self.ssn)
        
    def getowner(self):
        return self.ssn
    
    def removeOwn(ossn):
        removeOwner(ossn)
        
  