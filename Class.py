class Class:
    def __init__(self, database):
        self.class_no = None
        self.date = None
        self.time = None
        self.branch_no = 1
        self.tssn = None
        self.t_email = None
        self.t_id = None
        self.db = database

    def getAllClasses(self):
        results = self.db.getClassInfo()
        return results
        
        
    def addClass(self, no, date, time, ssn, id, email):
        self.class_no = no
        self.date = date
        self.time = time
        self.tssn = ssn
        self.t_email = email
        self.t_id = id
        createClass(no, date, time, self.branch_no, ssn, id, email)
         
        
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