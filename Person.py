from ConnectionGUI import *

class Person:
    
    def __init__(self,  database):
        self.ssn = None
        self.fname = None
        self.lname = None
        self.address = None
        self.phone = None
        self.email = None
        self.password = None
        self.db = database
        
        
        
    def addPerson(self, ssn, f, l, address, phone, email, password):
        self.ssn = ssn
        self.fname = f
        self.lname = l
        self.address = address
        self.phone = phone
        self.email = email
        self.password = password
        #create person inside the database
        self.db.createPerson(ssn, f, l, address, phone, email, password)
    
    def removePerson(self, ssn):
        self.db.deletePerson(ssn)
        
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