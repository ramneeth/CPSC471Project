from connection import *
from RestrictedUser import *
from Person import *

class Employee(RestrictedUser):
    
    def __init__(self, ssn, email, phone, f, l, address, password):
        self.ssn = ssn
        self.fname = f
        self.lname = l
        self.address = address
        self.phone = phone
        self.email = email
        self.password = password
        createEmployee(ssn, id, email, phone, f, l, address, password)
        self.id = getEmployeeID(ssn)
        
    def getEmployee(self):
        return self.ssn

    def addEmployee(self, person):
        self.id = getEmployeeID(person.ssn)
        addNewEmployee(person.ssn, person.fname, person.lname, person.address,
                    person.phone, person.email, self.id)
        
    def removeEmployee(self, ssn):
        removeEmp(ssn)