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
        # print("Checking for: "+email)
        self.cursor.execute("SELECT email FROM PERSON")
        results = self.cursor.fetchall()
        # print(results)
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

    def removeClient(self,email):
        self.cursor.execute("Select client_id FROM CLIENT WHERE client_email = %s GROUP BY client_email", (email,))
        results = self.cursor.fetchall()
        if (self.cursor.rowcount > 0):
            try:
                self.cursor.execute("DELETE FROM CLIENT WHERE client_id = %s;", results[0])
                self.connect.commit()
                return 0
            except Error as E:
                print("Error occured while deleting from client")
                return -1
        else:
            return -1

    def createMember(self, email):
        self.cursor.execute("Select * FROM client WHERE client_email = %s GROUP BY client_email", (email,))
        results = self.cursor.fetchall()
        if (self.cursor.rowcount > 0):
            # print(results)
            try:
                insert = "INSERT INTO MEMBER (mssn, client_id, member_email, fname, lname, member_pass, address, phone_number, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, 1)"
                values = results[0]
                self.cursor.execute(insert, values)
                self.connect.commit()
                return 0
            except Error as E:
                print("Error occured while inserting into member.")
                return -1
        else:
            return -1

    def removeMember(self,email):
        self.cursor.execute("Select membership_id FROM MEMBER WHERE member_email = %s GROUP BY member_email", (email,))
        results = self.cursor.fetchall()
        if (self.cursor.rowcount > 0):
            try:
                self.cursor.execute("DELETE FROM MEMBER WHERE membership_id = %s;", results[0])
                self.connect.commit()
                return 0
            except Error as E:
                print("Error occured while deleting from member")
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
        self.cursor.execute("Select * FROM TRAINER WHERE t_email = %s GROUP BY t_email", (email,))
        self.cursor.fetchall()
        if (self.cursor.rowcount > 0):
            return "trainer"
        self.cursor.execute("Select * FROM EMPLOYEE WHERE e_email = %s GROUP BY e_email", (email,))
        self.cursor.fetchall()
        if (self.cursor.rowcount > 0):
            return "employee"
        self.cursor.execute("Select * FROM MEMBER WHERE member_email = %s GROUP BY member_email", (email,))
        self.cursor.fetchall()
        if (self.cursor.rowcount > 0):
            return "member"
        self.cursor.execute("Select * FROM CLIENT WHERE client_email = %s GROUP BY client_email", (email,))
        self.cursor.fetchall()
        if (self.cursor.rowcount > 0):
            return "client"
        return "person"
        

    def getPersonInfo(self, email):
        self.cursor.execute("SELECT fname, lname, email, phone_number, address FROM PERSON WHERE email = %s;", (email,))
        data = self.cursor.fetchall()
        personArray = [data[0][0], data[0][1], data[0][2], data[0][3], data[0][4]]
        print(personArray)
        return personArray 
    
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
    
    def getSupplyInfo(self):
        self.cursor.execute("SELECT sname, supply_no, stock FROM SUPPLIES;")
        data = self.cursor.fetchall()
    
        suppArray = []
        for row in data:
            new = []
            new.append(row[0]) #appends the supply name
            new.append(row[1]) #appends the supply number
            new.append(row[2]) #appends the stock (amount)
            
            suppArray.append(new)
        return suppArray

    def getEquipInfo(self):
        self.cursor.execute("SELECT equipment_no, cdn, branch_no FROM EQUIPMENT;")
        data = self.cursor.fetchall()
        # print(data)
        equipArray = []
        for row in data:
            new = []
            new.append(row[0]) #appends the equipment no
            new.append(row[1]) #appends the date the equipment conditionh
            new.append(row[2]) #appends the branch number of the equipment

            equipArray.append(new)
        return equipArray

    def getRoomInfo(self):
        self.cursor.execute("SELECT room_id, date, duration FROM ROOMS;")
        data = self.cursor.fetchall()
        
        roomArray = []
        for row in data:
            new = []
            new.append(row[0]) #appends the room number
            new.append(row[1]) #appends the date it is booked on, if it is booked
            new.append(row[2]) #appends the duration in which it is booked
                
            roomArray.append(new)
        return roomArray

    def addBooking(self, roomid, date, duration):
        try:
            insert = "INSERT INTO ROOMS(room_id, date, duration) VALUES(%s, %s, %s);"
            values = (int(roomid), date, duration)
            self.cursor.execute(insert,values)
            self.connect.commit()
            return 0
        except Error as e:
            print("ERROR: Something went wrong when inserting into room")
            print(e)
            return -1

    def removeBooking(self, roomid, date, duration):
        try:
            delete = "DELETE FROM ROOMS WHERE room_id = %s AND date = %s AND duration = %s;"
            values = (int(roomid), date, duration)
            self.cursor.execute(delete,values)
            self.connect.commit()
            return 0
        except Error as e:
            print("ERROR: Something went wrong when inserting into room")
            print(e)
            return -1

    def addEquip(self, equipno, cdn):
        try:
            insert = "INSERT INTO EQUIPMENT(equipment_no, cdn, branch_no) VALUES(%s,%s,1);"
            values = (int(equipno),cdn)
            self.cursor.execute(insert,values)
            self.connect.commit()
            return 0
        except Error as e:
            print("ERROR: Something went wrong when inserting into equipment")
            print(e)
            return -1

    def UpdateEquip(self, equipno, cdn):
        try:
            update = "UPDATE EQUIPMENT SET cdn = %s WHERE equipment_no = %s AND branch_no = 1;"
            values = (cdn,int(equipno))
            self.cursor.execute(update,values)
            self.connect.commit()
            return 0
        except Error as e:
            print("ERROR: Something went wrong when updating equipment")
            print(e)
            return -1