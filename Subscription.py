from ConnectionGUI import *

class Subscription:
    def __init__(self, database):
        self.db = database
        
    def getStatus(self):
        return self.status
    
    def addSub(self, login, name):
        self.status = True
        self.db.createSubscription(login, name, self.status)
        
    def getSubs(self):
        return self.db.getSubscriptions()
    
    def setStatus(self, stat):
        self.status = stat
        self.db.updateSubscriptionStatus(self.status, self.login, self.branch_no)