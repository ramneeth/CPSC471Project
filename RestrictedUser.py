from connection import *
from Person import *

class RestrictedUser(Person):
    def __init__(self, ssn, email, phone, f, l, address, password):
        self.ssn = ssn
        self.fname = f
        self.lname = l
        self.address = address
        self.phone = phone
        self.email = email
        self.password = password
        createRUser(ssn, id, email, phone, f, l, address, password)
        self.id = getRUserID(ssn)
        
    def getRUser(self):
        return self.ssn

    def addRUser(self, person):
        self.id = getRUserID(self.ssn)
        addNewUser(person.ssn, person.fname, person.lname, person.address,
                    person.phone, person.email, self.id, person.password)
        
    def removeRU(self, ssn):
        removeRUser(ssn)
        
        
    def validateLogin(user, password):
        cursor.execute("SELECT email FROM PERSON")
        results = cursor.fetchall()
        for r in results:
            if user == r:
                query = "SELECT pass FROM PERSON WHERE email = %s;"
                value = user
                cursor.execute(query, value)
                res = cursor.fetchone()
                if password == res:
                    return True
                
        return False
    
    def changePass(username, password):
        query = "UPDATE PERSON SET pass = %s WHERE username = %s"
        values = (password, username)
        cursor.execute(query, values)
        connect.commit()
        
    def getEmployees():
        cursor.execute("SELECT fname, lname FROM EMPLOYEE")
        return cursor.fetchall()