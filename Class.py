from connection import *

class Class:
    def __init__(self, no, date, time, branch, ssn, id, email):
        self.class_no = no
        self.date = date
        self.time = time
        self.branch_no = branch
        self.tssn = ssn
        self.t_email = email
        createClass(no, date, time, branch, ssn, id, email)
        
    def getDate(self):
        return self.date
    
    def setDate(self, date):
        self.date = date
        updateClassDate(date, self.class_no)
        
    def changeTime(self, time):
        self.time = time
        updateClassTime(time, self.class_no, self.date)
        
    def changeInstructor(self, ssn, id, email):
        self.tssn = ssn
        self.t_id = id
        self.t_email = email
        updateClassInstructor(ssn, id, email, self.class_no)