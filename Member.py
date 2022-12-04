from connection import *
from Client import *

class Member(Client):
    def __init__(self, ssn, email, phone, f, l, address, memberID, status):
        self.ssn = ssn
        self.fname = f
        self.lname = l
        self.address = address
        self.phone = phone
        self.email = email
        self.memberID = memberID
        self.status = status
        createMember(ssn, id, email, phone, f, l, address,memberID, status)
        self.id = getMemberID(ssn)
        
        
    def getStatus(self, memberID):
        return self.status
        
    def changeStatus(self, memberID, stat):
        self.status = stat
        updateMemberStatus(memberID, stat)
        