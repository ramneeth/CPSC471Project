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
        try:
            insert = "INSERT INTO PERSON(ssn, fname, lname, address, pass, phone_number, email) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values =(ssn, f, l, address, passw, phone, email)
            self.cursor.execute(insert, values)
            self.connect.commit()
            return 0
        except Error as E:
            print(E)
            return -1

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

    def removeClient(self, email):
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
        
    def getClientID(self, email):
        self.cursor.execute("SELECT client_id FROM Client WHERE email = %s;", (email,))
        results = self.cursor.fetchall()
        return results[0]

    def getClientSSN(self, email):
        self.cursor.execute("SELECT cssn FROM CLIENT WHERE client_email = %s;", (email,))
        results = self.cursor.fetchall()
        return results[0]

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
        self.cursor.execute("Select * FROM PERSON WHERE email = %s GROUP BY email", (email,))
        results = self.cursor.fetchall()
        if (self.cursor.rowcount > 0):
            # print(results)
            try:
                insert = "INSERT INTO RESTRICTED_USER (rssn, fname, lname, address, r_pass, phone_number, r_email) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                values = results[0]
                self.cursor.execute(insert, values)
                self.connect.commit()
                return 0
            except Error as E:
                print("Error occured while inserting into restricted user.")
                print(E)
                return -1
        else:
            return -1
        
    def removeRUser(self, email):
        self.cursor.execute("Select r_email FROM RESTRICTED_USER WHERE r_email = %s GROUP BY r_email", (email,))
        results = self.cursor.fetchall()
        if (self.cursor.rowcount > 0):
            try:
                self.cursor.execute("DELETE FROM RESTRICTED_USER WHERE r_email = %s;", results[0])
                self.connect.commit()
                return 0
            except Error as E:
                print("Error occured while deleting from restricted user")
                return -1
        else:
            return -1
        
    def getRUserID(self, email):
        self.cursor.execute("SELECT r_user_id FROM RESTRICTED_USER WHERE r_email = %s;", (email,))
        results = self.cursor.fetchall()
        return results[0]

    def getRUserSSN(self, email):
        self.cursor.execute("SELECT rssn FROM RESTRICTED_USER WHERE r_email = %s;", (email,))
        results = self.cursor.fetchall()
        return results[0]

    def createEmployee(self, email):
        self.cursor.execute("SELECT rssn,r_user_id,fname,lname,address,r_pass,phone_number,r_email FROM RESTRICTED_USER WHERE r_email = %s GROUP BY r_email", (email,))
        results = self.cursor.fetchall()
        if (self.cursor.rowcount > 0):
            # print(results)
            try:
                insert = "INSERT INTO EMPLOYEE (essn, e_user_id,fname, lname, address, e_pass, phone_number, e_email,branch_no) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,1)"
                values = results[0]
                self.cursor.execute(insert, values)
                self.connect.commit()
                return 0
            except Error as E:
                print("Error occured while inserting into employee.")
                print(E)
                return -1
        else:
            return -1

    def removeEmployee(self, email):
        self.cursor.execute("Select e_user_id FROM EMPLOYEE WHERE e_email = %s GROUP BY e_email", (email,))
        results = self.cursor.fetchall()
        if (self.cursor.rowcount > 0):
            try:
                self.cursor.execute("DELETE FROM EMPLOYEE WHERE e_user_id = %s;", results[0])
                self.connect.commit()
                return 0
            except Error as E:
                print("Error occured while deleting from employee")
                print(E)
                return -1
        else:
            return -1
        
    def getEmpID(self, email):
        self.cursor.execute("SELECT e_user_id FROM EMPLOYEE WHERE e_email = %s;", (email,))
        results = self.cursor.fetchall()
        return results[0]

    def getEmpSSN(self, email):
        self.cursor.execute("SELECT essn FROM RESTRICTED_USER WHERE r_email = %s;", (email,))
        results = self.cursor.fetchall()
        return results[0]


    def createAssociate(self, email):
        self.cursor.execute("Select * FROM PERSON WHERE email = %s GROUP BY email", (email,))
        results = self.cursor.fetchall()
        if (self.cursor.rowcount > 0):
            # print(results)
            try:
                insert = "INSERT INTO ASSOCIATE (sssn, fname, lname, address, s_pass, phone_number, s_email) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                values = results[0]
                self.cursor.execute(insert, values)
                self.connect.commit()
                return 0
            except Error as E:
                print("Error occured while inserting into associate.")
                print(E)
                return -1
        else:
            return -1
        
    def getAssociateID(self, email):
        self.cursor.execute("SELECT s_user_id FROM ASSOCIATE WHERE s_email = %s;", (email,))
        results = self.cursor.fetchall()
        return results[0]

    def getAssociateSSN(self, email):
        self.cursor.execute("SELECT sssn FROM ASSOCIATE WHERE s_email = %s;", (email,))
        results = self.cursor.fetchall()
        return results[0]
    
    
    def createTrainer(self, email):
        self.cursor.execute("SELECT rssn,r_user_id,fname,lname,address,r_pass,phone_number,r_email FROM RESTRICTED_USER WHERE r_email = %s GROUP BY r_email", (email,))
        results = self.cursor.fetchall()
        if (self.cursor.rowcount > 0):
            # print(results)
            try:
                insert = "INSERT INTO TRAINER (tssn, t_user_id,fname, lname, address, t_pass, phone_number, t_email,branch_no) VALUES (%s, %s, %s, %s, %s, %s, %s, %s,1)"
                values = results[0]
                self.cursor.execute(insert, values)
                self.connect.commit()
                return 0
            except Error as E:
                print("Error occured while inserting into trainer.")
                print(E)
                return -1
        else:
            return -1
        
    def getTrainerID(self, email):
        self.cursor.execute("SELECT t_user_id FROM TRAINER WHERE t_email = %s;", (email,))
        results = self.cursor.fetchall()
        return results[0]

    def getTrainerSSN(self, email):
        self.cursor.execute("SELECT tssn FROM TRAINER WHERE t_email = %s;", (email,))
        results = self.cursor.fetchall()
        return results[0]

    def createAdmin(self, email):
        self.cursor.execute("Select * FROM PERSON WHERE email = %s GROUP BY email", (email,))
        results = self.cursor.fetchall()
        if (self.cursor.rowcount > 0):
            # print(results)
            try:
                insert = "INSERT INTO ADMIN (assn, fname, lname, address, admin_pass, phone_number, admin_email) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                values = results[0]
                self.cursor.execute(insert, values)
                self.connect.commit()
                return 0
            except Error as E:
                print("Error occured while inserting into admin.")
                print(E)
                return -1
        else:
            return -1

    def removeAdmin(self, email):
        self.cursor.execute("Select admin_id FROM ADMIN WHERE admin_email = %s GROUP BY admin_email", (email,))
        results = self.cursor.fetchall()
        if (self.cursor.rowcount > 0):
            try:
                self.cursor.execute("DELETE FROM ADMIN WHERE admin_id = %s;", results[0])
                self.connect.commit()
                return 0
            except Error as E:
                print("Error occured while deleting from admin")
                print(E)
                return -1
        else:
            return -1


    def getAdminID(self, email):
        self.cursor.execute("SELECT admin_id FROM ADMIN WHERE admin_email = %s;", (email,))
        results = self.cursor.fetchall()
        return results[0]
    
    def getAdminID(self, email):
        self.cursor.execute("SELECT assn FROM ADMIN WHERE admin_email = %s;", (email,))
        results = self.cursor.fetchall()
        return results[0]

    def createManager(self, email):
        self.cursor.execute("SELECT assn,fname,lname,address,admin_pass,phone_number,admin_email FROM ADMIN WHERE admin_email = %s GROUP BY admin_email", (email,))
        results = self.cursor.fetchall()
        if (self.cursor.rowcount > 0):
            # print(results)
            try:
                insert = "INSERT INTO MANAGER (mssn, fname, lname, address, m_pass, phone_number, m_email,branch_no) VALUES (%s, %s, %s, %s, %s, %s, %s,1 )"
                values = results[0]
                self.cursor.execute(insert, values)
                self.connect.commit()
                return 0
            except Error as E:
                print("Error occured while inserting into manager.")
                print(E)
                return -1
        else:
            return -1

    def removeManager(self, email):
        self.cursor.execute("Select m_id FROM MANAGER WHERE m_email = %s GROUP BY m_email", (email,))
        results = self.cursor.fetchall()
        if (self.cursor.rowcount > 0):
            try:
                self.cursor.execute("DELETE FROM MANAGER WHERE m_id = %s;", results[0])
                self.connect.commit()
                return 0
            except Error as E:
                print("Error occured while deleting from manager")
                print(E)
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
            return "client"
        self.cursor.execute("Select * FROM CLIENT WHERE client_email = %s GROUP BY client_email", (email,))
        self.cursor.fetchall()
        if (self.cursor.rowcount > 0):
            return "client"
        return "person"
        

    def getPersonInfo(self, email):
        self.cursor.execute("SELECT fname, lname, email, phone_number, address FROM PERSON WHERE email = %s;", (email,))
        data = self.cursor.fetchall()
        try:
            personArray = [data[0][0], data[0][1], data[0][2], data[0][3], data[0][4]]
            userType = self.checkUserType(email)
            personArray.append(userType)
            return personArray 
            # print(personArray)
        except Error as e:
            print("ERROR: Something went wrong when getting this person's info")
            return -1
    
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
        self.cursor.execute("SELECT equipment_no, equipment_name, cdn FROM EQUIPMENT;")
        data = self.cursor.fetchall()
        # print(data)
        equipArray = []
        for row in data:
            new = []
            new.append(row[0]) #appends the equipment no
            new.append(row[1]) #appends the date the equipment name
            new.append(row[2]) #appends the condition

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

    def addSupply(self, supplyno, supplyname, stock):
        try:
            insert = "INSERT INTO SUPPLIES(supply_no, sname, stock, branch_no) VALUES(%s,%s,%s,1);"
            values = (int(supplyno),supplyname,int(stock),)
            self.cursor.execute(insert,values)
            self.connect.commit()
            return 0
        except Error as E:
            print("ERROR: Something went wrong when inserting into supplies")
            print(e)
            return -1

    def updateSupply(self,supplyno,stock):
        try:
            update = "UPDATE SUPPLIES SET stock = %s WHERE supply_no = %s AND branch_no = 1;"
            values = (int(stock),int(supplyno))
            self.cursor.execute(update,values)
            self.connect.commit()
            return 0
        except Error as e:
            print("ERROR: Something went wrong when updating supply stock")
            print(e)
            return -1
        pass

    def addEquip(self, equipno, equipname, cdn, branch_no):
        try:
            insert = "INSERT INTO EQUIPMENT(equipment_no, equipment_name, amount, cdn, branch_no) VALUES(%s,%s, 1,%s,%s);"
            values = (int(equipno),equipname,cdn,branch_no)
            self.cursor.execute(insert,values)
            self.connect.commit()
            return 0
        except Error as e:
            print("ERROR: Something went wrong when inserting into equipment")
            print(e)
            return -1

    def updateEquip(self, equipno, cdn):
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

    
    def getWeeklySchedule(self, day):
        
        fullDay = []
        
        #get the email in the schedule for day 6-10
        self.cursor.execute("SELECT r_email FROM WEEKLY_SCHEDULE WHERE day_slots = %s AND time_slots = '6-10';", (day,))
        data = self.cursor.fetchall()
        
        self.cursor.execute("SELECT fname, lname FROM RESTRICTED_USER WHERE r_email = %s", data[0])
        name = self.cursor.fetchall()
        full_name = name[0][0] + " " + name[0][1] #store the full name together
        
        #insert the full name into the day list
        timeDay = ["6-10",full_name,data[0][0]]
        fullDay.append(timeDay)
        
        #get the email in the schedule for day 10-2
        self.cursor.execute("SELECT r_email FROM WEEKLY_SCHEDULE WHERE day_slots = %s AND time_slots = '10-2';", (day,))
        data = self.cursor.fetchall()
        
        self.cursor.execute("SELECT fname, lname FROM RESTRICTED_USER WHERE r_email = %s", data[0])
        name = self.cursor.fetchall()
        full_name = name[0][0] + " " + name[0][1] #store the full name together
        
        #insert the full name into the day list
        timeDay = ["10-2",full_name,data[0][0]]
        fullDay.append(timeDay)
        
        #get the email in the schedule for day 2-6
        self.cursor.execute("SELECT r_email FROM WEEKLY_SCHEDULE WHERE day_slots = %s AND time_slots = '2-6';", (day,))
        data = self.cursor.fetchall()
        
        self.cursor.execute("SELECT fname, lname FROM RESTRICTED_USER WHERE r_email = %s", data[0])
        name = self.cursor.fetchall()
        full_name = name[0][0] + " " + name[0][1] #store the full name together
        
        #insert the full name into the day list
        timeDay = ["2-6",full_name,data[0][0]]
        fullDay.append(timeDay)
        
        #get the email in the schedule for day 6-12
        self.cursor.execute("SELECT r_email FROM WEEKLY_SCHEDULE WHERE day_slots = %s AND time_slots = '6-12';", (day,))
        data = self.cursor.fetchall()
        
        self.cursor.execute("SELECT fname, lname FROM RESTRICTED_USER WHERE r_email = %s", data[0])
        name = self.cursor.fetchall()
        full_name = name[0][0] + " " + name[0][1] #store the full name together
        
        #insert the full name into the day list
        timeDay = ["6-12",full_name,data[0][0]]
        fullDay.append(timeDay)
        
        #return the  array for one full day
        #[6-10,10-2,2-6,6-12]
        return fullDay


    def addTimeSlot(self, email, day, timeslot):
        try:
            insert = "INSERT INTO WEEKLY_SCHEDULE(r_email, time_slots, day_slots, branch_no) VALUES(%s,%s,%s,1);"
            values = (email,timeslot,day,)
            self.cursor.execute(insert,values)
            self.connect.commit()
            return 0
        except Error as E:
            print("Error: Something went wrong when inserting into schedule")
            print(E)
            return -1


    def removeTimeSlot(self, email, day, timeslot):
        try:
            delete = "DELETE FROM WEEKLY_SCHEDULE WHERE r_email = %s AND time_slots = %s AND day_slots = %s;"
            values = (email, timeslot, day,)
            self.cursor.execute(delete,values)
            self.connect.commit()
            return 0
        except Error as E:
            print("Error: Something went wrong when removing from schedule")
            print(E)
            return -1

    def createOwner(self, email):
        self.cursor.execute("Select * FROM PERSON WHERE email = %s GROUP BY email", (email,))
        results = self.cursor.fetchall()
        if (self.cursor.rowcount > 0):
            # print(results)
            try:
                insert = "INSERT INTO OWNER (ossn, fname, lname, address, owner_pass, phone_number, owner_email, Branch_num) VALUES (%s, %s, %s, %s, %s, %s, %s,1)"
                values = results[0]
                self.cursor.execute(insert, values)
                self.connect.commit()
                return 0
            except Error as E:
                print("Error occured while inserting into owner.")
                return -1
        else:
            return -1
        
        
    def createGym(self, loc, manager, owner):
        insert = ("INSERT INTO GYM(branch_no, location, ossn, mssn) VALUES (%s, %s, %s, %s)")
        values = (loc,manager,owner,)
        self.cursor.execute(insert,values)
        self.connect.commit()
        results = self.cursor.fetchall()
        if (self.cursor.rowcount > 0):
            return 0
        else:
            return -1

    def createSubscription(self, login, name):
        insert = ("INSERT INTO SUBSCRIPTION(login_id, name, status) VALUES (%s, %s, %s)")
        values = (login,name,1,)
        self.cursor.execute(insert,values)
        self.connect.commit()
        results = self.cursor.fetchall()
        if (self.cursor.rowcount > 0):
            return 0
        else:
            return -1
        
    def getSubscriptions(self):
        self.cursor.execute("SELECT login_id, name, status FROM SUBSCRIPTION;")
        data = self.cursor.fetchall()
        subs = []
       
        for row in data:
            new = []
            new.append(row[0]) #append the login id
            new.append(row[1]) #append the name
            if(row[2] == 1):
                new.append('Active')
            else:
                new.append('Unactive')
            
            subs.append(new)
            
        return subs
    
        
        
        
    
