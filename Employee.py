from RestrictedUser import *

class Employee(RestrictedUser):
    
    def __init__(self, database):
        self.ssn = None
        self.fname = None
        self.lname = None
        self.address = None
        self.phone = None
        self.email = None
        self.password = None
        self.db = database

    def createEmployee(self, email):
        results = self.db.createRUser(email)
        if (results == -1):
            return -1
        else:
            results = self.db.createEmployee(email)
            if (results == -1):
                return -1
            else:
                return 0
        
        
    def addEmployee(self, ssn, email, phone, f, l, address, password):
        self.ssn = ssn
        self.fname = f
        self.lname = l
        self.address = address
        self.phone = phone
        self.email = email
        self.password = password
        self.db.createEmployee(ssn, email, phone, f, l, address, password)
        self.id = getEmployeeID(ssn)
            
        
    def getEmployee(self):
        return self.ssn

    def addEmployee(self, person):
        self.id = getEmployeeID(person.ssn)
        addNewEmployee(person.ssn, person.fname, person.lname, person.address,
                    person.phone, person.email, self.id)
        
    def removeEmployee(self, email):
        results = self.db.removeEmployee(email)
        if (results != -1):
            results = self.db.removeRUser(email)
            if (results != -1):
                return 0
            else: return -1
        else: return -1