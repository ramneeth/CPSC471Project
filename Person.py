from ConnectionGUI import *

class Person:
    
    def __init__(self, database):
        # self.ssn = None
        # self.fname = None
        # self.lname = None
        # self.address = None
        # self.phone = None
        # self.email = None
        # self.password = None
        self.db = database
        #create person inside the database

    def getPersonInfo(self, email):
        results = self.db.getPersonInfo(email)
        return results

    def checkUserType(self, email):
        result = self.db.checkUserType(email)
        return result
        
    def validateLogin(self, email,passw):
        result = self.db.validateLogin(email,passw)
        return result

    def createPerson(self, ssn, f, l, address, phone, email, password):
        self.db.createPerson(ssn, f, l, address, password, phone, email)
