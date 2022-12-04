from connection import *
from Employee import *

class Associate(Employee):
    def __init__(self, ssn, email, phone, f, l, address, branch):
        self.ssn = ssn
        self.fname = f
        self.lname = l
        self.address = address
        self.phone = phone
        self.email = email
        self.branch = branch
        createAssociate(ssn, id, email, phone, f, l, address, branch)
        self.id = getAssociateID(ssn)
        
    def getAssociate(self):
        return self.ssn
        
    def removeAssociate(self, ssn):
        deleteAssociate(ssn)
        
    def setEquipment(self, e):
        self.equipment = e