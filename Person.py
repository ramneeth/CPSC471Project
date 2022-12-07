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

    def removePerson(self, ssn):
        deletePerson(ssn)
        
    def getName(self):
        fullName = self.fname + self.lname
        return fullName
    
    def getPhone(self):
        return self.phone

    def getEmail(self):
        return self.email
    
    def getSsn(self):
        return self.ssn
    
    def changeName(self,last):
        self.lname = last
        #update database with new last name
        updatePersonName(self.ssn, last)
        
    def changePhone(self, phone):
        self.phone = phone
        #update database with new phone
        updatePersonPhone(self.ssn, phone)
        
    def changeEmail(self, email):
        self.email = email
        #update database with new email
        updatePersonEmail(self.ssn, email)
        
    def changeAddress(self, address):
        self.address = address
        #update person's address
        updatePersonAddress(self.ssn, address)
        
    def changePassword(self, password):
        self.password = password
        username = self.username
        changePass(password, username)