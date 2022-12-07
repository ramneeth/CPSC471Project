from ConnectionGUI import *

class Supplies:
    def __init__(self, database):
        self.db = database

    def getAllSupplies(self):
        results = self.db.getSupplyInfo()
        return results

    def addSupply(self,no, name, stock):
        results = self.db.addSupply(no,name,stock)
        return results
        
    def updateStock(self, no, stock):
        results = self.db.updateSupply(no, stock)
        return results
    