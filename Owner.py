from ConnectionGUI import *
from Admin import *

class Owner(Admin):
    def __init__(self, database):
        self.ssn = 123456789
        self.fname = "Jalal"
        self.lname = "Kawash"
        self.address = "2500 University Dr NW, Calgary, AB T2N 1N4"
        self.phone = 4034034033
        self.email = "jalal.kawash@ucalgary.ca"
        self.password = "cpsc"
        self.db = database
        results = self.db.createPerson(self.ssn, self.fname, self.lname, self.address, self.phone, self.email, self.password)
        if (results != -1):
            self.db.createOwner(self.email)
        
    def getowner(self):
        return self.ssn
        
        
  