from ConnectionGUI import *
from Employee import *

class Associate(Employee):
    def __init__(self, database):
        self.ssn = None
        self.fname = None
        self.lname = None
        self.address = None
        self.phone = None
        self.email = None
        self.branch = None
        self.db = database
        
        
    def addAssociate(self, ssn, email, phone, f, l, address):
        self.ssn = ssn
        self.email = email
        self.phone = phone
        self.fname = f
        self.lname = l
        self.address = address
        self.db.createAssociate(ssn, email, phone, f, l, address, self.branch)
        self.id = self.db.getAssociateID(ssn)
    
    def getAssociate(self):
        return self.ssn
        
    def removeAssociate(self, ssn):
        self.db.deleteAssociate(ssn)
        
    def setEquipment(self, e):
        self.equipment = e