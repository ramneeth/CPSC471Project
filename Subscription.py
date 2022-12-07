from ConnectionGUI import *

class Subscription:
    def __init__(self, login, name, database):
        self.login = login
        self.name = name
        self.status = True
        self.branch_no = 1
        self.db = database
        self.db.createSubscription(login, name, self.status, self.branch_no)
        
    def getStatus(self):
        return self.status
    
    def setStatus(self, stat):
        self.status = stat
        self.db.updateSubscriptionStatus(self.status, self.login, self.branch_no)