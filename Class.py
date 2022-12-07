from ConnectionGUI import *

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
        
        