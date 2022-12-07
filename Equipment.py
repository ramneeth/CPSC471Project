from ConnectionGUI import *

class Equipment:
    def __init__(self, database):
        self.no = None
        self.amount = None
        self.condition = None
        self.branch = 1
        self.equipment_name = None
        self.db = database
        
    def getAllEquipment(self):
        results = self.db.getEquipInfo()
        return results
        
    def createEquipment(self, no, name, condition):
        result = self.db.addEquip(no, name, condition, self.branch)
        return result
        
    def updateEquip(self, no, condition):
        result = self.db.updateEquip(no, condition)
        return result
        