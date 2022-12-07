from ConnectionGUI import *
from Employee import *
from Room import *

class Trainer(Employee):
    def __init__(self, database):
        self.ssn = None
        self.ssn = None
        self.id = None
        self.db = database
  
    def addTrainr(self,email):
        self.email = email
        self.db.createTrainer(email)
        self.id = self.getTrainerID(email)
        self.ssn = self.db.getTrainerSSN(email)
        

