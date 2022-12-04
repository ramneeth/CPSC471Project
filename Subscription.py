from connection import *

class Subscription:
    def __init__(self, login, name):
        self.login = login
        self.name = name
        self.status = True
        self.branch_no = 1
        createSubscription(login, name, self.status, self.branch_no)
        
    def getStatus(self):
        return self.status
    
    def setStatus(self, stat):
        self.status = stat
        updateSubscriptionStatus(self.status, self.login, self.branch_no)