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
        self.db = database
        
        
    def addGym(self, loc, manager, owner):
        self.location = loc
        self.manager = manager
        self.owner = owner
        resutls = self.db.createGym(self.branch, loc, owner, manager)
        
        
    def addSubscription(self, login, name):
        self.sub = Subscription(login, name, self.branch_no)
        self.db.createSubscription(login, name, True)
        