from Client import *
from ConnectionGUI import *

class Member(Client):
    def __init__(self, database):
        self.db = database
        
    def createMember(self, email):
        results = self.db.createMember(email)
        return results

    def removeMember(self, email):
        results = self.db.removeMember(email)
        return results

    def getStatus(self, memberID):
        return self.status