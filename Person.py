from ConnectionGUI import *

class Person:
    
    def __init__(self, ssn, f, l, address, phone, email, password, database):
        self.ssn = ssn
        self.fname = f
        self.lname = l
        self.address = address
        self.phone = phone
        self.email = email
        self.password = password
        self.db = database
        #create person inside the database
        self.db.createPerson(ssn, f, l, address, phone, email, password)
        
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