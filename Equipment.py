from connection import *
from Associate import *

class Equipment:
    def __init__(self, database):
        self.no = None
        self.amount = None
        self.condition = None
        self.branch = 1
        self.equipment_name = None
        self.db = database
        
        
    def createEquipment(self, no, amount, condition, name):
        self.no = no
        self.amount = amount
        self.condition = condition
        self.equipment_name = name
        self.db.createEquip(no, amount, condition, self.branch, name)
        
    def updateCondition(self, status):
        self.db.updateEquipCond(self.no, status)
        self.status = status
        
    def addAmount(self):
        self.db.updateEquipAmount(self.no)
        self.amount = self.amount +1
    
    def getAmount(self):
        return self.amount
    
    def getCondition(self):
        return self.condition