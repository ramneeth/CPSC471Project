class Supplies:
    def __init__(self, database):
        self.db = database

    def getAllSupplies(self):
        results = self.db.getSupplyInfo()
        return results
        
    def updateStock(branch, name, number, stock):
        updateSupplyStock(stock, number, branch)
    
    def getStock(self):
        return self.stock
    
    def getName(self):
        return self.sname