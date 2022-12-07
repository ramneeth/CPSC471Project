
from Admin import *

class Manager(Admin):
    def __init__(self, database):
        self.ssn = None
        self.fname = None
        self.lname = None
        self.address = None
        self.phone = None
        self.email = None
        self.branch = 1
        self.db = database
        

    def createManager(self, email):
        results = self.db.createAdmin(email)
        if (results != -1):
            results = self.db.createManager(email)
            if (results != -1):
                return 0
            else: return -1
        else: return -1

    def removeManager(self, email):
        results = self.db.removeManager(email)
        if (results != -1):
            results = self.db.removeAdmin(email)
            if (results != -1):
                return 0
            else: return -1
        else: return -1
        
    # def createManager(self, ssn, email, phone, f, l, address):
    #     self.db.createManager(ssn, email, phone, f, l, address, self.branch)
    #     self.id = getManagerID(ssn)
        
    def getManager(self):
        return self.ssn
    
    def getID(self):
        return self.id
    
    def getBranch(self):
        return self.branch