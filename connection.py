import mysql.connector
from mysql.connector import Error
from array import *

try:
    connect = mysql.connector.connect(user = 'final', password = 'cpsc', 
                                        host = '127.0.0.1', database = 'gym_database')
    if connect.is_connected():
        cursor = connect.cursor()
        
        
except Error as e:
    print("Error occured while connecting.\n username, password or database name incorrect.\n")

#create an new person in the Person table
def createPerson(self, ssn, f, l, address, phone, email):
        insert = "INSERT INTO PERSON(ssn, fname, lname, address, phone_number, email) VALUES (%s, %s, %s, %s, %s, %s)"
        values =(ssn, f, l, address, int(phone), email)
        self.cursor.execute(insert, values)
        self.connect.commit()

#delete an existing person
def deletePerson(self, ssn):
    sql = "DELETE FROM PERSON WHERE ssn = %s;"
    values = (ssn)
    self.cursor.execute(sql, values)
    self.connect.commit()
    
#update person's last name
def updatePersonName(self, ssn, lname):
    sql = "UPDATE PERSON SET lname = %s WHERE ssn = %s;"
    values = (lname, ssn)
    self.cursor.execute(sql, values)
    self.connect.commit()
    
#update person's phone number
def updatePersonPhone(self, ssn, phone):
    sql = "UPDATE PERSON SET phone_number = %s WHERE ssn = %s;"
    values = (phone, ssn)
    self.cursor.execute(sql, values)
    self.connect.commit()
    
#update person's email
def updatePersonEmail(self, ssn, email):
    sql = "UPDATE PERSON SET email = %s WHERE ssn = %s;"
    values = (email, ssn)
    self.cursor.execute(sql, values)    
    self.connect.commit()
    
#update person's address
def updatePersonAddress(self, ssn, address):
    sql = "UPDATE PERSON SET address = %s WHERE ssn = %s;"
    values = (address, ssn)
    self.cursor.execute(sql, values)
    self.connect.commit()


#create a client 
def createClient(self, ssn, id, email, phone, f, l, address):
    sql = "INSERT INTO CLIENT(cssn, client_id, fname, lname, address, phone_number, client_email)\
                    VALUES(%s, %s, %s, %s, %s, %s, %s)"
    values = (ssn, id, f, l, address, phone, email)
    self.cursor.execute(sql, values)
    self.connect.commit()
    
def addNewClient(self,ssn, fname, lname, address, phone, email, id):
    sql = "INSERT INTO CLIENT(cssn, client_id, fname, lname, address, phone_number, client_email)\
                    VALUES(%s, %s, %s, %s, %s, %s, %s)"
    values = (ssn, id, fname, lname, address, phone, email)
    self.cursor.execute(sql, values)
    self.connect.commit()

#remove a client
def removeClient(self, ssn):
    sql = "DELETE FROM CLIENT WHERE ssn = %s;"
    values = (ssn)
    self.cursor.execute(sql,values)
    self.connect.commit()

def removeAdmin(self, ssn):
    sql = "DELETE FROM ADMIN WHERE ssn = %s;"
    values = (ssn)
    self.cursor.execute(sql, values)
    self.connect.commit()
    
def createAdmin(self, ssn, id, email, phone, f, l, address):
    sql = "INSERT INTO ADMIN(assn, admin_id, admin_email, fname, lname, address, phone_number)\
                    VALUES(%s, %s, %s, %s, %s, %s, %s);"
    values = ssn, id, f, l, address, phone, email
    self.cursor.execute(sql, values)
    self.connect.commit()
    
def addNewAdmin(self,ssn, fname, lname, address, phone, email, id):
    sql = "INSERT INTO ADMIN(assn, admin_id, admin_email, fname, lname, address, phone_number)\
                    VALUES(%s, %s, %s, %s, %s, %s, %s)"
    values = (ssn, id, fname, lname, address, phone, email)
    self.cursor.execute(sql, values)
    self.connect.commit()

def removeRUser(self, ssn):
    sql = "DELETE FROM RESTRICTED_USER WHERE ssn = %s;"
    values = (ssn)
    self.cursor.execute(sql, values)
    self.connect.commit()
    
def createRUser(self, ssn, id, email, phone, f, l, address):
    sql = "INSERT INTO RESTRICTED_USER(assn, admin_id, admin_email, fname, lname, address, phone_number)\
                    VALUES(%s, %s, %s, %s, %s, %s, %s)"
    values = (ssn, id, f, l, address, phone, email)
    self.cursor.execute(sql, values)
    self.connect.commit()
    
def addNewUser(self,ssn, fname, lname, address, phone, email, id):
    sql = "INSERT INTO RESTRICTED_USER(rssn, r_user_id, r_user_email, fname, lname, address, phone_number)\
                    VALUES(%s, %s, %s, %s, %s, %s, %s)"
    values = (ssn, id, fname, lname, address, phone, email)
    self.cursor.execute(sql, values)
    self.connect.commit()
    
def createEmployee(self, ssn, id, email, phone, f, l, address):
    sql = "INSERT INTO EMPLOYEE(essn, e_user_id, e_email, fname, lname, address, phone_number)\
                    VALUES(%s, %s, %s, %s, %s, %s, %s)"
    values = (ssn, id, f, l, address, phone, email)
    self.cursor.execute(sql, values)
    self.connect.commit()
    
def addNewEmployee(self, ssn, fname, lname, address, phone, email, id):
    sql = "INSERT INTO EMPLOYEE(essn, e_user_id, e_email, fname, lname, address, phone_number)\
                    VALUES(%s, %s, %s, %s, %s, %s, %s);"
    values = (ssn, id, fname, lname, address, phone, email)
    self.cursor.execute(sql, values)
    self.connect.commit()
    
def removeEmp(self, ssn):
    sql = "DELETE FROM EMPLOYEE WHERE ssn = %s;"
    values = (ssn)
    self.cursor.execute(sql, values)
    self.connect.commit()

def createOwner(self, ossn, owner_id, owner_email, Branch_num, f, l, address, phone_number):
    sql = "INSERT INTO OWNER(ossn, owner_id, owner_email, Branch_num, fname, lname, address, phone_number)\
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (ossn, owner_id, owner_email, Branch_num, f, l, address, phone_number)
    self.cursor.execute(sql, values)
    self.connect.commit()
    
def removeOwner(self, ossn):
    sql = "DELETE FROM OWNER WHERE ossn = %s;"
    values = (ossn)
    self.cursor.execute(sql, values)
    self.connect.commit()
    
def createAssociate(self, ssn, id, email, phone, f, l, address, branch):
    sql = "INSERT INTO ASSOCIATE(sssn, s_user_id, s_email, fname, lname, address, phone_number, branch_no)\
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s);"
    values = (ssn, id, f, l, address, phone, email, branch)
    self.cursor.execute(sql, values)
    self.connect.commit()
    
def deleteAssociate(self, ssn):
    sql = "DELETE FROM ASSOCIATE WHERE ssn = %s;"
    values = (ssn)
    self.cursor.execute(sql, values)
    self.connect.commit()
    
def createManager(self, mssn, m_id, m_email, branch_no, f, l, address, phone_number):
    sql = "INSERT INTO MANAGER(mssn, m_id, m_email, branch_no, f, l, address, phone_number)\
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (mssn, m_id, m_email, branch_no, f, l, address, phone_number)
    self.cursor.execute(sql, values)
    self.connect.commit()

def createTrainer(self, ssn, id, email, phone, f, l, address, branch):
    sql = "INSERT INTO TRAINER(tssn, t_user_id, t_email, fname, lname, address, phone_number, branch_no)\
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s);"
    values = (ssn, id, f, l, address, phone, email, branch)
    self.cursor.execute(sql, values)
    self.connect.commit()

def deleteTrainer(self, ssn):
    sql = "DELETE FROM TRAINER WHERE ssn = %s;"
    values = (ssn)
    self.cursor.execute(sql, values)
    self.connect.commit()

def addClassToTrainer(self, class_no, tssn):
    sql = "UPDATE TRAINER SET class_no = %s WHERE tssn = %s;"
    values = (class_no, tssn)
    self.cursor.execute(sql, values)
    self.connect.commit()

def createMember(self, mssn, client_id, membership_id, member_email, type, status, f, l, address, phone_number):
    sql = "INSERT INTO MEMBER(mssn, client_id, membership_id, member_email, type, status, f, l, address, phone_number)\
                    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (mssn, client_id, membership_id, member_email, type, status, f, l, address, phone_number)
    self.cursor.execute(sql, values)
    self.connect.commit()

def updateMemberStatus(self, membership_id, status):
    sql = "UPDATE MEMBER SET status = %s WHERE membership_id = %s;"
    values = (status, membership_id)
    self.cursor.execute(sql, values)
    self.connect.commit()

def updateScheduleAvail(self, day, r_user_id):
    sql = "UPDATE WEEKLY_SCHEDULE_AVAIL SET day = %s WHERE r_user_id = %s;"
    values = (day,r_user_id)
    self.cursor.execute(sql, values)
    self.connect.commit()

def createClass(self, class_no, date, time, branch_no, t_id, t_email, tssn):
    sql = "INSERT INTO CLASS(class_no, date, time, branch_no, t_id, t_email, tssn) VALUES(%s, %s, %s, %s, %s, %s, %s);"
    values = (class_no, date, time, branch_no, t_id, t_email, tssn)    
    self.cursor.execute(sql, values)
    self.connect.commit()

def updateClassDate(self, date, class_no):
    sql = "UPDATE CLASS SET date = %s WHERE class_no = %s;"
    values = (date, class_no)
    self.cursor.execute(sql, values)
    self.connect.commit()

def updateClassTime(self, time, class_no):
    sql = "UPDATE CLASS SET time = %s WHERE class_no = %s;"
    values = (time, class_no)
    self.cursor.execute(sql, values)
    self.connect.commit()

def updateClassInstructor(self, tssn, t_id, t_email, class_no):
    sql = "UPDATE CLASS SET tssn = %s, t_id = %s, t_email = %s WHERE class_no = %s;"
    values = (tssn, t_id, t_email, class_no)
    self.cursor.execute(sql, values)
    self.connect.commit()

def createRoom(self, room_id, date, duration):
    sql = "INSERT INTO ROOM(room_id, date, duration) VALUES(%s, %s, %s);"
    values = (room_id, date, duration)
    self.cursor.execute(sql, values)
    self.connect.commit()

def cancelBooking(self, room_id, date, duration):
    sql = "DELETE FROM ROOMS WHERE room_id = %s, date = %s, duration = %s;"
    values = (room_id, date, duration)
    self.cursor.execute(sql, values)
    self.connect.commit()

def updateEquipCond(self, condition, equipment_no, branch_no):
    sql = "UPDATE EQUIPTMENT SET condition = %s WHERE equipment_no = %s AND branch_no = %s;"
    values = (condition, equipment_no, branch_no)
    self.cursor.execute(sql, values)
    self.connect.commit()

def createEquip(self, equipment_no, amount, condition,branch_no):
    sql = "INSERT INTO EQUIPMENT(equipment_no, amount, condition, branch_no) VALUES(%s, %s, %s, %s, %s);"
    values = (equipment_no, amount, condition, branch_no)
    self.cursor.execute(sql, values)
    self.connect.commit()

def updateEquipAmount(self, amount, equipment_no, branch_no):
    sql = "UPDATE EQUIPMENT SET amount = %s WHERE equipment_no = %s AND branch_no = %s;"
    values = (amount, equipment_no, branch_no)
    self.cursor.execute(sql, values)
    self.connect.commit()

def createSupply(self, sname, supply_no, stock, branch_no):
    sql = "INSERT INTO SUPPLY(sname, supply_no, stock, branch_no) VALUES(%s, %s, %s, %s);"
    values = (sname, supply_no, stock, branch_no)
    self.cursor.execute(sql, values)
    self.connect.commit()

def updateSupplyStock(self, stock, supply_no, branch_no):
    sql = "UPDATE SUPPLIES SET stock = %s WHERE supply_no = %s AND branch_no = %s;"
    values = (stock, supply_no, branch_no)
    self.cursor.execute(sql, values)
    self.connect.commit()

def createGym(self, branch_no, location, o_ssn, mssn):
    sql = "INSERT INTO SUBSCRIPTION(branch_no, location, o_ssn, mssn) VALUES(%s, %s, %s, %s);"
    values = (branch_no, location, o_ssn, mssn)
    self.cursor.execute(sql, values)
    self.connect.commit()

#create new subscription
def createSubscription(self, login_id, name,status,branch_no):
    sql = "INSERT INTO SUBSCRIPTION(login_id, name, status, branch_no) VALUES (%s, %s, %s, %s);"
    values = (login_id, name,status,branch_no)
    self.cursor.execute(sql, values)
    self.connect.commit()

def updateSubscriptionStatus(self, status, login_id, branch_no):
    sql = "UPDATE SUBSCRIPTION SET status = %s WHERE login_id = %s AND branch_no = %s;"
    values = (status, login_id, branch_no)
    self.cursor.execute(sql, values)
    self.connect.commit()

#getters for the id's for all the different types of people
def getRUserID(ssn):
    cursor.execute("SELECT rssn FROM RESTRICTED_USER WHERE ssn = %s;", ssn)
    return cursor.fetchall()

def getManagerID(ssn):
    cursor.execute("SELECT mssn FROM MANAGER WHERE ssn = %s;", ssn)
    return cursor.fetchall()
def getRUserID(ssn):
    cursor.execute("SELECT rssn FROM RESTRICTED_USER WHERE ssn = %s;", ssn)
    return cursor.fetchall()
def getEmployeeID(ssn):
    cursor.execute("SELECT essn FROM EMPLOYEE WHERE ssn = %s;", ssn)
    return cursor.fetchall()
def getClientID(ssn):
    cursor.execute("SELECT cssn FROM CLIENT WHERE ssn = %s;", ssn)
    return cursor.fetchall()
def getAdminID(ssn):
    cursor.execute("SELECT assn FROM ADMIN WHERE ssn = %s;", ssn)
    return cursor.fetchall()
def getAssociateID(ssn):
    cursor.execute("SELECT sssn FROM ASSOCIATE WHERE ssn = %s;", ssn)
    return cursor.fetchall()
def getTrainerID(ssn):
    cursor.execute("SELECT tssn FROM TRAINER WHERE ssn = %s;", ssn)
    return cursor.fetchall()
def getMemberID(ssn):
    cursor.execute("SELECT mssn FROM MEMBER WHERE ssn = %s;", ssn)
    return cursor.fetchall()
def getOwnerID(ssn):
    cursor.execute("SELECT ossn FROM OWNER WHERE ssn = %s;", ssn)
    return cursor.fetchall()

#https://pynative.com/python-cursor-fetchall-fetchmany-fetchone-to-read-rows-from-table/
def getClasses():
    cursor.execute("SELECT date, time, t_email FROM CLASS;")
    data = cursor.fetchall()
    
    classArray = []
    for row in data:
        cursor.execute("SELECT fname, lname FROM TRAINER WHERE t_email = %s;", (row[2],))
        name = cursor.fetchone()
        new = []
        new.append(row[0])
        new.append(row[1])
        new.append(row[2])
        new.append(name[0] + name[1])
        
            
        classArray.append(new)
    return classArray

#function to retrieve all the information about the equipment in the database
def getEquipment():
    cursor.execute("SELECT equipment_no, cdn, amount, equipment_name FROM EQUIPMENT;")
    data = cursor.fetchall()
    
    equipArray = []
    for row in data:
        new = []
        new.append(row[0]) #appends the equipment number
        new.append(row[1]) #appends the condition
        new.append(row[2]) #appends the amount
        new.append(row[3]) #appends the name
        
            
        equipArray.append(new)
    return equipArray

#function to retrieve all the information about the supplies in the database
def getSupplies():
    cursor.execute("SELECT sname, supply_no, stock FROM SUPPLIES;")
    data = cursor.fetchall()
    
    suppArray = []
    for row in data:
        new = []
        new.append(row[0]) #appends the supply name
        new.append(row[1]) #appends the supply number
        new.append(row[2]) #appends the stock (amount)
        
            
        suppArray.append(new)
    return suppArray

#function to retrieve all the information about the subscriptions in the database
def getSubs():
    cursor.execute("SELECT login_id FROM SUBSCRIPTION;")
    data = cursor.fetchall()
    
    subArray = []
    for row in data:
        new = []
        new.append(row[0]) #appends the login id
        subArray.append(new)
        
    return subArray

#function to retrieve all the information about the rooms in the database
def getRooms():
    cursor.execute("SELECT room_id, date, duration FROM ROOMS;")
    data = cursor.fetchall()
    
    roomArray = []
    for row in data:
        new = []
        new.append(row[0]) #appends the room number
        new.append(row[1]) #appends the date it is booked on, if it is booked
        new.append(row[2]) #appends the duration in which it is booked
        
            
        roomArray.append(new)
    return roomArray

#function to get all the employee information to create the weekly schedule
def getEmployees():
    cursor.execute("SELECT fname, lname, e_mail FROM EMPLOYEES;")
    data = cursor.fetchall()
    
    empArray = []
    for row in data:
        new = []
        new.append(row[0]) #appends the employee's first name
        new.append(row[1]) #appends the employee's last name
        new.append(row[2]) #appends the employee's email
        
            
        empArray.append(new)
    return empArray
    
def changePass(self,username, password):
    self.cursor.execute("UPDATE PERSON SET pass = %s WHERE email = %s GROUP BY email", (password, username,))
    connect.commit()

connect.close()