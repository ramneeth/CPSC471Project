from connection import *
from Employee import *
from Room import *

class Trainer(Employee):
    def __init__(self, database):
        self.ssn = None
        self.fname = None
        self.lname = None
        self.address = None
        self.phone = None
        self.email = None
        self.branch = 1
        self.db = database
  
    def addTrainr(self, ssn, email, phone, f, l, address):
        self.ssn = ssn
        self.fname = f
        self.lname = l
        self.address = address
        self.phone = phone
        self.email = email
        createAssociate(ssn, id, email, phone, f, l, address, self.branch)
        self.id = getTrainerID(ssn)
        
        
    def getTrainer(self):
        return self.ssn
        
    def removeTrainer(self, ssn):
        deleteTrainer(ssn)
