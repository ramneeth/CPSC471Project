from ConnectionGUI import *
from Subscription import *
from Employee import *
from Owner import *
from Manager import *

class Gym:
    def __init__(self, database):
        self.branch = 1
        self.location = None
        self.manager = None
        self.owner = None
        
        
    def addGym(self, loc, manager, owner):
        self.location = loc
        self.manager = manager
        self.owner = owner
        self.db.createGym(self.branch, loc, owner, manager)
        
        
    def addSubscription(self, login, name):
        self.sub = Subscription(login, name, self.branch_no)
        createSubscription(login, name, True, self.branch_no)
        
    def changeOwner(self, owner):
        self.owner = owner
        
    def getOwner(self):
        return self.owner.getOwner()
    
    def getLocation(self):
        return self.location
    
    def getSubscriptions(self):
        return self.sub