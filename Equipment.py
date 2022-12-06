from connection import *
from Associate import *

class Equipment:
    def __init__(self, no, amount, condition, name, database):
        self.no = no
        self.amount = amount
        self.condition = condition
        self.branch = 1
        self.equipment_name = name
        self.db = database
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