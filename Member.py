from connection import *
from Client import *

class Member(Client):
    def __init__(self, database):
        self.ssn = None
        self.fname = None
        self.lname = None
        self.address = None
        self.phone = None
        self.email = None
        self.memberID = None
        self.status = None
    
    def addMember(ssn, email, phone, f, l, address, memberID, status):
        self.db.createMember(ssn, id, email, phone, f, l, address,memberID, status)
        self.id = getMemberID(ssn)
        
    def getStatus(self, memberID):
        return self.status
        
    def changeStatus(self, memberID, stat):
        self.status = stat
        updateMemberStatus(memberID, stat)
        