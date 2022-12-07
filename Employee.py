from RestrictedUser import *
from ConnectionGUI import *

class Employee(RestrictedUser):
    
    def __init__(self, database):
        self.email = None
        self.ssn = None
        self.id = None
        self.db = database

    def createEmployee(self, email):
        self.email = email
        results = self.db.createRUser(email)
        if (results == -1):
            return -1
        else:
            results = self.db.createEmployee(email)
            if (results == -1):
                return -1
            else:
                self.id = self.db.getEmpID(email)
                self.ssn = self.db.getEmpSSN(email)
                return 0
        
    def removeEmployee(self, email):
        results = self.db.removeEmployee(email)
        if (results != -1):
            results = self.db.removeRUser(email)
            if (results != -1):
                return 0
            else: return -1
        else: return -1