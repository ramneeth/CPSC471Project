from connection import *
from Admin import *

class Manager(Admin):
    def __init__(self, ssn, email, phone, f, l, address,branch):
        self.ssn = ssn
        self.fname = f
        self.lname = l
        self.address = address
        self.phone = phone
        self.email = email
        self.branch = branch
        createManager(ssn, email, phone, f, l, address, branch)
        self.id = getManagerID(ssn)
        
    def getManager(self):
        return self.ssn
    
    def getID(self):
        return self.id
    
    def getBranch(self):
        return self.branch