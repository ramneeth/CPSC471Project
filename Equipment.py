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
        result = self.db.createEquip(no, name, condition, self.branch_no)
        return result
        
    def updateCondition(self, no, condition):
        result = self.db.updateEquipCond(no, condition)
        return result
        
    def addAmount(self):
        self.db.updateEquipAmount(self.no)
        self.amount = self.amount +1
    
    def getAmount(self):
        return self.amount
    
    def getCondition(self):
        return self.condition