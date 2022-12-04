from connection import *

class Supplies:
    def __init__(self, branch, sname, supply, stock):
        self.branch_no = branch
        self.sname = sname
        self.supply_no = supply
        self.stock = stock
        createSupply(sname, supply, stock, branch)
        
    def updateStock(branch, name, number, stock):
        updateSupplyStock(stock, number, branch)
    
    def getStock(self):
        return self.stock
    
    def getName(self):
        return self.sname