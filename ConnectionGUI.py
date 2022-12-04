import mysql.connector
from mysql.connector import Error
from array import *

#MAKE SURE TO RENAME THIS FILE TO 'Connection' BEFORE USING WITH THE GUI!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Database:

    def __init__(self):
        self.connect = None
        self.cursor = None
        self.load()

    def load(self):
        self.connect = mysql.connector.connect(user = 'final', password = 'cpsc', 
                                            host = '127.0.0.1', database = 'gym_database')
        if self.connect.is_connected():
            self.cursor = self.connect.cursor()
        # except Error as e:
        #     print("Error occured while connecting.\n username, password or database name incorrect.\n")

    def close(self):
        self.connect.close()

    def validateLogin(self, email, passw):
        print("Checking for: "+email)
        self.cursor.execute("SELECT email FROM PERSON")
        results = self.cursor.fetchall()
        print(results)
        for  r in results:
            if email == r[0]:
                query = "SELECT pass FROM PERSON WHERE email = %(email)s"
                self.cursor.execute(query, {'email' : email})
                res = self.cursor.fetchone()
                if passw == res[0]:
                    return True
                else:
                    return False
        return False

# create an new person in the Person table
    def createPerson(self, ssn, f, l, address, passw, phone, email):
        insert = "INSERT INTO PERSON(ssn, fname, lname, address, pass, phone_number, email) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values =(ssn, f, l, address, passw, int(phone), email)
        self.cursor.execute(insert, values)
        self.connect.commit()

# create a new client from the email of a person
    def createClient(self, email):
        self.cursor.execute("Select * FROM PERSON WHERE email = %s GROUP BY email", (email,))
        results = self.cursor.fetchall()
        if (self.cursor.rowcount > 0):
            # print(results)
            try:
                insert = "INSERT INTO CLIENT (cssn, fname, lname, address, client_pass, phone_number, client_email) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                values = results[0]
                self.cursor.execute(insert, values)
                self.connect.commit()
                return 0
            except Error as E:
                print("Error occured while inserting into client.")
                return -1
        else:
            return -1

    def createRUser(self, email):
        results = self.getPerson(email)
        if (self.cursor.rowcount > 0):
            try:
                sql = "INSERT INTO RESTRICTED_USER(rssn, fname, lname, address, r_pass, phone_number, r_email)\
                                VALUES(%s, %s, %s, %s, %s, %s, %s)"
                values = results[0]
                self.cursor.execute(sql, values)
                self.connect.commit()
                return 0
            except Error as E:
                print("Error occured while inserting into Restricted_User.")
                return -1
        else:
            return -1


    def getPerson(self, email):
        self.cursor.execute("Select * FROM PERSON WHERE email = %s GROUP BY email", (email,))
        results = self.cursor.fetchall()
        return results

        # def createEmployee(self, email):
        #     self.cursor.execute("SELECT * FROM PERSON WHERE email = %s GROUP by email", (email,))
        #     results = self.cursor.fetchall()
        #     if (self.cursor.rowcount > 0):
        #         try:
        #             sql = "INSERT INTO EMPLOYEE(essn, fname, lname, address, e_pass, phone_number, e_email, branch_no)\
        #                     VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
        #             values = results[0]
        #             self.cursor.execute(sql, values)
        #             self.connect.commit()
        #         except Error as E:
        #             print("Error has occured while inserting into client.")
        #             return -1
        #     else:
        #         return -1

    def checkUserType(self, email):
        self.cursor.execute("Select * FROM OWNER WHERE owner_email = %s GROUP BY owner_email", (email,))
        self.cursor.fetchall()
        if (self.cursor.rowcount > 0):
            return "owner"
        self.cursor.execute("Select * FROM ADMIN WHERE admin_email = %s GROUP BY admin_email", (email,))
        self.cursor.fetchall()
        if (self.cursor.rowcount > 0):
            return "admin"
        self.cursor.execute("Select * FROM RESTRICTED_USER WHERE r_email = %s GROUP BY r_email", (email,))
        self.cursor.fetchall()
        if (self.cursor.rowcount > 0):
            return "ruser"
        self.cursor.execute("Select * FROM EMPLOYEE WHERE e_email = %s GROUP BY e_email", (email,))
        self.cursor.fetchall()
        if (self.cursor.rowcount > 0):
            return "employee"
        self.cursor.execute("Select * FROM CLIENT WHERE client_email = %s GROUP BY client_email", (email,))
        self.cursor.fetchall()
        if (self.cursor.rowcount > 0):
            return "client"
        return "person"
        

    # def getInfoFromEmail(self,email):
    #     self.cursor.execute("SELECT fname, lname, email, phone_number, address FROM PERSON WHERE email = %s GROUP BY email", (email,))
    #     results = self.cursor.fetchall()
    #     if (self.cursor.rowcount > 0):
    #         print(results)
    #         for info in results[0]:

                
    
    # https://pynative.com/python-cursor-fetchall-fetchmany-fetchone-to-read-rows-from-table/
    def getClassInfo(self):
        self.cursor.execute("SELECT date, time, t_email FROM CLASS;")
        data = self.cursor.fetchall()
        # print(data)
        classArray = []
        for row in data:
            self.cursor.execute("SELECT fname FROM TRAINER WHERE t_email = %s;", (row[2],))
            fname = self.cursor.fetchone()
            self.cursor.execute("SELECT lname FROM TRAINER WHERE t_email = %s;", (row[2],))
            lname = self.cursor.fetchone()
            new = []
            new.append(row[0])
            new.append(row[1])
            new.append(row[2])
            new.append(fname[0])
            new.append(lname[0])
                
            classArray.append(new)

        return classArray

    # def getEquipInfo(self):
    #     self.cursor.execute("SELECT date, time, t_email FROM CLASS;")
    #     data = self.cursor.fetchall()
    #     # print(data)
    #     classArray = []
    #     for row in data:
    #         self.cursor.execute("SELECT fname FROM TRAINER WHERE t_email = %s;", (row[2],))
    #         fname = self.cursor.fetchone()
    #         self.cursor.execute("SELECT lname FROM TRAINER WHERE t_email = %s;", (row[2],))
    #         lname = self.cursor.fetchone()
    #         new = []
    #         new.append(row[0])
    #         new.append(row[1])
    #         new.append(row[2])
    #         new.append(fname[0])
    #         new.append(lname[0])
                
    #         classArray.append(new)

    #     return classArray

#     #delete an existing person
#     def deletePerson(ssn):
#         cursor.execute("DELETE FROM PERSON WHERE ssn = %s;", ssn)
#         connect.commit()
        
#     #update person's last name
#     def updatePersonName(ssn, lname):
#         cursor.execute("UPDATE PERSON SET lname = %s WHERE ssn = %s;", lname, ssn)
#         connect.commit()
        
#     #update person's phone number
#     def updatePersonPhone(ssn, phone):
#         cursor.execute("UPDATE PERSON SET phone_number = %s WHERE ssn = %s;", phone, ssn)
#         connect.commit()
        
#     #update person's email
#     def updatePersonEmail(ssn, email):
#         cursor.execute("UPDATE PERSON SET email = %s WHERE ssn = %s;", email, ssn)    
#         connect.commit()
        
#     #update person's address
#     def updatePersonAddress(ssn, address):
#         cursor.execute("UPDATE PERSON SET address = %s WHERE ssn = %s;", address, ssn)
#         connect.commit()
        
#     #create a client 
#     def createClient(ssn, id, email, phone, f, l, address):
#         cursor.execute("INSERT INTO CLIENT(cssn, client_id, fname, lname, address, phone_number, client_email)\
#                         VALUES(%s, %s, %s, %s, %s, %s, %s)", ssn, id, f, l, address, phone, email)
#         cursor.commit()
        
#     def addNewClient(self,ssn, fname, lname, address, phone, email, id):
#         cursor.execute("INSERT INTO CLIENT(cssn, client_id, fname, lname, address, phone_number, client_email)\
#                         VALUES(%s, %s, %s, %s, %s, %s, %s)", ssn, id, fname, lname, address, phone, email)
#         connect.commit()

#     #remove a client
#     def removeClient(ssn):
#         cursor.execute("DELETE FROM CLIENT WHERE ssn = %s;", ssn)
#         connect.commit()

#     def removeAdmin(ssn):
#         cursor.execute("DELETE FROM ADMIN WHERE ssn = %s;", ssn)
#         connect.commit()
        
#     def createAdmin(ssn, id, email, phone, f, l, address):
#         cursor.execute("INSERT INTO ADMIN(assn, admin_id, admin_email, fname, lname, address, phone_number)\
#                         VALUES(%s, %s, %s, %s, %s, %s, %s)", ssn, id, f, l, address, phone, email)
#         connect.commit()
        
#     def addNewAdmin(self,ssn, fname, lname, address, phone, email, id):
#         cursor.execute("INSERT INTO ADMIN(assn, admin_id, admin_email, fname, lname, address, phone_number)\
#                         VALUES(%s, %s, %s, %s, %s, %s, %s)", ssn, id, fname, lname, address, phone, email)
#         connect.commit()

#     def removeRUser(ssn):
#         cursor.execute("DELETE FROM RESTRICTED_USER WHERE ssn = %s;", ssn)
#         connect.commit()
        
#     def createRUser(ssn, id, email, phone, f, l, address):
#         cursor.execute("INSERT INTO RESTRICTED_USER(assn, admin_id, admin_email, fname, lname, address, phone_number)\
#                         VALUES(%s, %s, %s, %s, %s, %s, %s)", ssn, id, f, l, address, phone, email)
#         connect.commit()
        
#     def addNewUser(self,ssn, fname, lname, address, phone, email, id):
#         cursor.execute("INSERT INTO RESTRICTED_USER(rssn, r_user_id, r_user_email, fname, lname, address, phone_number)\
#                         VALUES(%s, %s, %s, %s, %s, %s, %s)",ssn, id, fname, lname, address, phone, email)
#         connect.commit()
        
#     def createEmployee(ssn, id, email, phone, f, l, address):
#         cursor.execute("INSERT INTO EMPLOYEE(essn, e_user_id, e_email, fname, lname, address, phone_number)\
#                         VALUES(%s, %s, %s, %s, %s, %s, %s)", ssn, id, f, l, address, phone, email)
#         connect.commit()
        
#     def addNewEmployee(ssn, fname, lname, address, phone, email, id):
#         cursor.execute("INSERT INTO EMPLOYEE(essn, e_user_id, e_email, fname, lname, address, phone_number)\
#                         VALUES(%s, %s, %s, %s, %s, %s, %s);", ssn, id, fname, lname, address, phone, email)
#         connect.commit()
        
#     def removeEmp(ssn):
#         cursor.execute("DELETE FROM EMPLOYEE WHERE ssn = %s;", ssn)
#         connect.commit()

#     def createOwner(ossn, owner_id, owner_email, Branch_num, f, l, address, phone_number):
#         cursor.execute("INSERT INTO OWNER(ossn, owner_id, owner_email, Branch_num, fname, lname, address, phone_number)\
#                         VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", ossn, owner_id, owner_email, Branch_num, f, l, address, phone_number)
#         connect.commit()
        
#     def removeOwner(ossn):
#         cursor.execute("DELETE FROM OWNER WHERE ossn = %s;", ossn)
#         connect.commit()
        
#     def createAssociate(ssn, id, email, phone, f, l, address, branch):
#         cursor.execute("INSERT INTO ASSOCIATE(sssn, s_user_id, s_email, fname, lname, address, phone_number, branch_no)\
#                         VALUES(%s, %s, %s, %s, %s, %s, %s, %s);",ssn, id, f, l, address, phone, email, branch)
#         connect.commit()
        
#     def deleteAssociate(ssn):
#         cursor.execute("DELETE FROM ASSOCIATE WHERE ssn = %s;", ssn)
#         connect.commit()
        
#     def createManager(mssn, m_id, m_email, branch_no, f, l, address, phone_number):
#         cursor.execute("INSERT INTO MANAGER(mssn, m_id, m_email, branch_no, f, l, address, phone_number)\
#                         VALUES(%s, %s, %s, %s, %s, %s, %s, %s)", mssn, m_id, m_email, branch_no, f, l, address, phone_number)
#         connect.commit()

#     def createTrainer(ssn, id, email, phone, f, l, address, branch):
#         cursor.execute("INSERT INTO TRAINER(tssn, t_user_id, t_email, fname, lname, address, phone_number, branch_no)\
#                         VALUES(%s, %s, %s, %s, %s, %s, %s, %s);",ssn, id, f, l, address, phone, email, branch)
#         connect.commit()

#     def deleteTrainer(ssn):
#         cursor.execute("DELETE FROM TRAINER WHERE ssn = %s;", ssn)
#         connect.commit()

#     def addClassToTrainer(class_no, tssn):
#         cursor.execute("UPDATE TRAINER SET class_no = %s WHERE tssn = %s;", class_no, tssn)
#         connect.commit()

#     def createMember(mssn, client_id, membership_id, member_email, type, status, f, l, address, phone_number):
#         cursor.execute("INSERT INTO MEMBER(mssn, client_id, membership_id, member_email, type, status, f, l, address, phone_number)\
#                         VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", mssn, client_id, membership_id, member_email, type, status, f, l, address, phone_number)
#         connect.commit()

#     def updateMemberStatus(membership_id, status):
#         cursor.execute("UPDATE MEMBER SET status = %s WHERE membership_id = %s;", status, membership_id)
#         connect.commit()

#     def updateMemberType(membership_id, type):
#         cursor.execute("UPDATE MEMBER SET type = %s WHERE membership_id = %s;", type, membership_id)
#         connect.commit()

#     def updateScheduleAvail(day, r_user_id):
#         cursor.execute("UPDATE WEEKLY_SCHEDULE_AVAIL SET day = %s WHERE r_user_id = %s;", day,r_user_id)
#         connect.commit()

#     def createClass(class_no, date, time, branch_no, t_id, t_email, tssn):
#         cursor.execute("INSERT INTO CLASS(class_no, date, time, branch_no, t_id, t_email, tssn) VALUES(%s, %s, %s, %s, %s, %s, %s);", class_no, date, time, branch_no, t_id, t_email, tssn)
#         connect.commit()

#     def updateClassDate(date, class_no):
#         cursor.execute("UPDATE CLASS SET date = %s WHERE class_no = %s;", date, class_no)
#         connect.commit()

#     def updateClassTime(time, class_no):
#         cursor.execute("UPDATE CLASS SET time = %s WHERE class_no = %s;",time, class_no)
#         connect.commit()

#     def updateClassInstructor(tssn, t_id, t_email, class_no):
#         cursor.execute("UPDATE CLASS SET tssn = %s, t_id = %s, t_email = %s WHERE class_no = %s;", tssn, t_id, t_email, class_no)
#         connect.commit()

#     def createRoom(room_id, date, duration):
#         cursor.execute("INSERT INTO ROOM(room_id, date, duration) VALUES(%s, %s, %s);", room_id, date, duration)
#         connect.commit()

#     def cancelBooking(room_id, date, duration):
#         cursor.execute("DELETE FROM ROOMS WHERE room_id = %s, date = %s, duration = %s;",room_id, date, duration )
#         connect.commit()

#     def updateEquipCond(condition, equipment_no, branch_no):
#         cursor.execute("UPDATE EQUIPTMENT SET condition = %s WHERE equipment_no = %s AND branch_no = %s;", condition, equipment_no, branch_no)
#         connect.commit()

#     def createEquip(equipment_no, amount, condition, duration, branch_no):
#         cursor.execute("INSERT INTO EQUIPMENT(equipment_no, amount, condition, duration, branch_no) VALUES(%s, %s, %s, %s, %s);", equipment_no, amount, condition, duration, branch_no)
#         connect.commit()

#     def updateEquipAmount(amount, equipment_no, branch_no):
#         cursor.execute("UPDATE EQUIPMENT SET amount = %s WHERE equipment_no = %s AND branch_no = %s;", amount, equipment_no, branch_no)
#         connect.commit()

#     def createSupply(sname, supply_no, stock, branch_no):
#         cursor.execute("INSERT INTO SUPPLY(sname, supply_no, stock, branch_no) VALUES(%s, %s, %s, %s);", sname, supply_no, stock, branch_no)
#         connect.commit()

#     def updateSupplyStock(stock, supply_no, branch_no):
#         cursor.execute("UPDATE SUPPLIES SET stock = %s WHERE supply_no = %s AND branch_no = %s;", stock, supply_no, branch_no)
#         connect.commit()

#     def createGym(branch_no, location, o_ssn, mssn):
#         cursor.execute("INSERT INTO SUBSCRIPTION(branch_no, location, o_ssn, mssn) VALUES(%s, %s, %s, %s);", branch_no, location, o_ssn, mssn)
#         connect.commit()

#     #create new subscription
#     def createSubscription(login_id, name,status,branch_no):
#         cursor.execute("INSERT INTO SUBSCRIPTION(login_id, name, status, branch_no) VALUES (%s, %s, %s, %s);",login_id, name,status,branch_no)
#         connect.commit()

#     def updateSubscriptionStatus(status, login_id, branch_no):
#         cursor.execute("UPDATE SUBSCRIPTION SET status = %s WHERE login_id = %s AND branch_no = %s;", status, login_id, branch_no)
#         connect.commit()

#     def getRUserID(ssn):
#         cursor.execute("SELECT rssn FROM RESTRICTED_USER WHERE ssn = %s;", ssn)
#         return cursor.fetchall()

#     def getManagerID(ssn):
#         cursor.execute("SELECT mssn FROM MANAGER WHERE ssn = %s;", ssn)
#         return cursor.fetchall()
#     def getRUserID(ssn):
#         cursor.execute("SELECT rssn FROM RESTRICTED_USER WHERE ssn = %s;", ssn)
#         return cursor.fetchall()
#     def getRUserID(ssn):
#         cursor.execute("SELECT rssn FROM RESTRICTED_USER WHERE ssn = %s;", ssn)
#         return cursor.fetchall()
#     def getRUserID(ssn):
#         cursor.execute("SELECT rssn FROM RESTRICTED_USER WHERE ssn = %s;", ssn)
#         return cursor.fetchall()
#     def getRUserID(ssn):
#         cursor.execute("SELECT rssn FROM RESTRICTED_USER WHERE ssn = %s;", ssn)
#         return cursor.fetchall()
#     def getRUserID(ssn):
#         cursor.execute("SELECT rssn FROM RESTRICTED_USER WHERE ssn = %s;", ssn)
#         return cursor.fetchall()