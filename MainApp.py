import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from ConnectionGUI import Database
from Person import Person
from Class import Class
from Supplies import Supplies
from Equipment import Equipment
from Room import Room
from Client import Client
from Member import Member
from Employee import Employee
from Manager import Manager
from WeeklySchedule import WeeklySchedule

db = Database()
person = Person(db)
classes = Class(db)
supplies = Supplies(db)
equipment = Equipment(db)
rooms = Room(db)
client = Client(db)
member = Member(db)
employee = Employee(db)
manager = Manager(db)
schedule = WeeklySchedule(db)
loggedInEmail = None

class RegForm(Screen):

    fname = ObjectProperty(None)
    lname = ObjectProperty(None)
    email = ObjectProperty(None)
    addr = ObjectProperty(None)
    phone = ObjectProperty(None)
    ssn = ObjectProperty(None)
    passw = ObjectProperty(None)
    pass

    def submit(self):
        fields = [self.fname,self.lname,self.email,self.addr,self.phone,self.ssn,self.passw]
        
        for field in fields:
            if (field.text == ""):
                self.invalidReg("empty")
                return 1

        if (self.email.text.find("@") != -1 and self.email.text.find(".") != -1):
            if len(self.phone.text) == 10:
                if len(self.ssn.text) == 9:
                    person.createPerson(self.ssn.text,self.fname.text,self.lname.text,self.addr.text,self.phone.text,
                                        self.email.text, self.passw.text)
                    # db.createPerson(self.ssn.text, self.fname.text, self.lname.text, 
                    #                 self.addr.text, self.passw.text, self.phone.text, self.email.text)
                    # print("Name: ", self.fname.text, self.lname.text)
                    # print("Email: ", self.email.text)
                    # print("Address: ", self.addr.text)
                    # print("Phone Number: ", self.phone.text)
                    # print("SSN: ", self.ssn.text)
                    # print("Password: ",self.passw.text)
                    self.reset()
                    return 0
                else:
                    self.invalidReg("ssn")
                    return 1
            else:
                self.invalidReg("phone")
                return 1
        else:
            self.invalidReg("email")
            return 1
    
    def reset(self):
        self.fname.text = ""
        self.lname.text = ""
        self.email.text = ""
        self.addr.text = ""
        self.phone.text = ""
        self.ssn.text = ""
        self.passw.text = ""

    def invalidReg(self,type):
        if (type == "empty"):
            pop = Popup(title = "Error while creating account",
                        content = Label(text="Please fill in all fields."),
                        size_hint=(None,None), size=(400,200))
            pop.open()
        if (type == "email"):
            pop = Popup(title = "Error while creating account",
                        content = Label(text="Invalid email."),
                        size_hint=(None,None), size=(400,200))
            pop.open()
        elif (type == "phone"):
            pop = Popup(title = "Error while creating account",
                        content = Label(text="Invalid phone number."),
                        size_hint=(None,None), size=(400,200))
            pop.open()
        elif (type == "ssn"):
            pop = Popup(title = "Error while creating account",
                        content = Label(text="Invalid SSN."),
                        size_hint=(None,None), size=(400,200))
            pop.open()


class LoginForm(Screen):
    email = ObjectProperty(None)
    passw = ObjectProperty(None)
    userType = "ruser"
    pass
    def submit(self):
        # print("Email:", self.email.text)
        # print("Password:", self.passw.text)
        # return 0
        # db.createClient("testclient@gmail.com")
        # db.getInfoFromEmail("i.d@ucalgary.ca")
        print(db.getClassInfo())
        if (self.email.text == "" or self.passw.text == ""):
            self.invalidLogin("empty")
            self.userType = None
            return -1
        elif (self.email.text.find("@") == -1 or self.email.text.find(".") == -1 ):
            self.invalidLogin("email")
            self.userType = None
            return -1
        else:
            if (not db.validateLogin(self.email.text, self.passw.text)):
                print("LOGIN FAILED")
                self.invalidLogin("invalid")
                self.userType = None
                return -1
            else:
                usertype = db.checkUserType(self.email.text)
                if (usertype == "person"):
                    self.invalidLogin("person")
                    self.userType = "person"
                    return -1
                else:
                    print("SUCCESS LOGIN")
                    global loggedInEmail
                    loggedInEmail = self.email.text
                    self.email.text = ""
                    self.passw.text = ""
                    self.userType = usertype
                    return 0
    def invalidLogin(self,type):
        if (type == "empty"):
            pop = Popup(title = "Login",
                    content = Label(text="ERROR: Please fill in all fields"),
                    size_hint=(None,None), size=(400,200))
            pop.open()
        elif (type == "email"):
            pop = Popup(title = "Login",
                    content = Label(text="ERROR: Invalid email"),
                    size_hint=(None,None), size=(400,200))
            pop.open()
        elif (type == "invalid"):
            pop = Popup(title = "Login",
                    content = Label(text="ERROR: Invalid credentials"),
                    size_hint=(None,None), size=(400,200))
            pop.open()
        elif (type == "person"):
            pop = Popup(title = "Login",
                    content = Label(text="ERROR: Account not yet confirmed. Visit the front desk"),
                    size_hint=(None,None), size=(400,200))
            pop.open()



class ThreeFieldLine(BoxLayout):
    pass

class FourFieldLine(BoxLayout):
    pass

class FiveFieldLine(BoxLayout):
    pass

class ModifySchedulePopup(Popup):
    r_email = ObjectProperty(None)
    date = None
    time_slot = None
    pass

    def addTimeSlot(self):
        if (self.r_email.text == "" or self.date == None or self.time_slot == None):
            pop = Popup(title = "Modify Schedule",
                    content = Label(text="ERROR: Please fill in all fields and select a day and timeslot."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
        elif (self.r_email.text.find("@") == -1 or self.r_email.text.find(".") == -1):
            pop = Popup(title = "Modify Schedule",
                    content = Label(text="ERROR: Invalid email."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
        elif (person.checkUserType(self.r_email.text) != "ruser"):
            pop = Popup(title = "Modify Schedule",
                    content = Label(text="ERROR: Cannot add this account to the schedule."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
        else:
            result = schedule.addTimeSlot(self.r_email.text,self.date,self.time_slot)
            if (result == 0):
                pop = Popup(title = "Modify Schedule",
                    content = Label(text="Successfully scheduled."),
                    size_hint=(None,None), size=(400,200))   
                pop.open()
                self.r_email.text = ""
                self.date = None
                self.time_slot = None
            else:
                pop = Popup(title = "Modify Schedule",
                    content = Label(text="Error: Possible duplicate entry."),
                    size_hint=(None,None), size=(400,200))
                pop.open()

    def removeTimeSlot(self):
        if (self.r_email.text == "" or self.date == None or self.time_slot == None):
            pop = Popup(title = "Modify Schedule",
                    content = Label(text="ERROR: Please fill in all fields and select a day and timeslot."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
        elif (self.r_email.text.find("@") == -1 or self.r_email.text.find(".") == -1):
            pop = Popup(title = "Modify Schedule",
                    content = Label(text="ERROR: Invalid email."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
        else:
            result = schedule.removeTimeSlot(self.r_email.text,self.date,self.time_slot)
            if (result == 0):
                pop = Popup(title = "Modify Schedule",
                    content = Label(text="Successfully removed schedule."),
                    size_hint=(None,None), size=(400,200))   
                pop.open()
                self.r_email.text = ""
                self.date = None
                self.time_slot = None
            else:
                pop = Popup(title = "Modify Schedule",
                    content = Label(text="Error: Something went wrong when trying to remove schedule."),
                    size_hint=(None,None), size=(400,200))
                pop.open()

class ModifySuppliesPopup(Popup):
    pass

class ModifyEquipmentPopup(Popup):
    equipno = ObjectProperty(None)
    equipname = ObjectProperty(None)
    condition = None
    pass

    def addEquipment(self):
        if (self.equipno.text == "" or self.equipname.text == "" or self.condition == None):
            pop = Popup(title = "Modify Equipment",
                    content = Label(text="ERROR: Please fill in all fields and select a condition."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
        elif (not self.equipno.text.isnumeric()):
            pop = Popup(title = "Modify Equipment",
                    content = Label(text="ERROR: Invalid input."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
        else:
            result = equipment.createEquipment(self.equipno.text,self.equipname.text,self.condition)
            if (result == 0):
                pop = Popup(title = "Modify Equipment",
                    content = Label(text="Successfully created equipment."),
                    size_hint=(None,None), size=(400,200))   
                pop.open()
                self.equipno.text = ""
            else:
                pop = Popup(title = "Modify Equipment",
                    content = Label(text="Error: Something went wrong when trying to create equipment."),
                    size_hint=(None,None), size=(400,200))
                pop.open()

    def updateEquipment(self):
        if (self.equipno.text == "" or self.condition == ""):
            pop = Popup(title = "Modify Equipment",
                    content = Label(text="ERROR: Please fill in all fields and select a condition."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
        elif (not self.equipno.text.isnumeric()):
            pop = Popup(title = "Modify Equipment",
                    content = Label(text="ERROR: Invalid input."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
        else:
            result = equipment.UpdateConditon(self.equipno.text,self.condition)
            if (result == 0):
                pop = Popup(title = "Modify Equipment",
                    content = Label(text="Successfully updated equipment."),
                    size_hint=(None,None), size=(400,200))   
                pop.open()
                self.equipno.text = ""
                self.condition = None
            else:
                pop = Popup(title = "Modify Equipment",
                    content = Label(text="Error: Something went wrong when trying to update equipment."),
                    size_hint=(None,None), size=(400,200))
                pop.open()


class ModifyBookingPopup(Popup):
    roomid = ObjectProperty(None)
    date = None
    duration = ObjectProperty(None)
    pass

    def addBooking(self):
        if (self.roomid.text == "" or self.date == None or self.duration.text == ""):
            pop = Popup(title = "Modify Booking",
                    content = Label(text="ERROR: Please fill in all fields and select a day."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
        elif (not self.roomid.text.isnumeric() or self.duration.text.isnumeric()):
            pop = Popup(title = "Modify Booking",
                    content = Label(text="ERROR: Invalid input."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
        else:
            result = rooms.addBooking(self.roomid.text,self.date,self.duration.text)
            if (result == 0):
                pop = Popup(title = "Modify Booking",
                    content = Label(text="Successfully booked."),
                    size_hint=(None,None), size=(400,200))   
                pop.open()
                self.roomid.text = ""
                self.date = None
                self.duration.text = ""
            else:
                pop = Popup(title = "Modify Booking",
                    content = Label(text="Error: Something went wrong when trying to book."),
                    size_hint=(None,None), size=(400,200))
                pop.open()

    def removeBooking(self):
        if (self.roomid.text == "" or self.date == "" or self.duration.text == ""):
            pop = Popup(title = "Modify Booking",
                    content = Label(text="ERROR: Please fill in all fields."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
        elif (self.roomid.text.isalpha() or self.duration.text.isalpha()):
            pop = Popup(title = "Modify Booking",
                    content = Label(text="ERROR: Invalid input."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
        else:
            result = rooms.removeBooking(self.roomid.text,self.date,self.duration.text)
            if (result == 0):
                pop = Popup(title = "Modify Booking",
                    content = Label(text="Successfully removed booking."),
                    size_hint=(None,None), size=(400,200))   
                pop.open()
                self.roomid.text = ""
                self.duration.text = ""
            else:
                pop = Popup(title = "Modify Booking",
                    content = Label(text="Error: Something went wrong when trying to remove booking."),
                    size_hint=(None,None), size=(400,200))
                pop.open()


class AdminHomepage(Screen):
    client_email = ObjectProperty(None)
    client_fname = ObjectProperty(None)
    client_lname = ObjectProperty(None)
    client_demail = ObjectProperty(None)
    client_phone = ObjectProperty(None)
    client_addr = ObjectProperty(None)
    client_usertype = ObjectProperty(None)
    user_fname = ObjectProperty(None)
    user_lname = ObjectProperty(None)
    user_email = ObjectProperty(None)
    user_phone = ObjectProperty(None)
    user_addr = ObjectProperty(None)
    pass 

    def __init__(self, **kwargs):
        super(AdminHomepage, self).__init__(**kwargs)
        # print(array)
        # self.accountInfo.data = 
        self.classes.data = [{'label_1': str(x['date']), 'label_2': str(x['time']), 'label_3': str(x['email']), 'label_4': x['fname'], 'label_5': x['lname']} for x in self.getClasses()]
        self.supplies.data = [{'label_1': str(x['supplyno']), 'label_2': str(x['supplyname']), 'label_3': str(x['stock'])} for x in self.getSupplies()]
        self.equipment.data = [{'label_1': str(x['equipno']), 'label_2': str(x['cdn']), 'label_3': str(x['branchno'])} for x in self.getEquip()]
        self.rooms.data = [{'label_1': str(x['roomid']), 'label_2': str(x['date']), 'label_3': str(x['duration'])} for x in self.getRooms()]
        # self.getScheduleInfo()
        self.getScheduleInfo()
        # print(self.supplies.data)



    def on_enter(self):
        self.getCurrentAccountInfo(loggedInEmail)
    

    def getCurrentAccountInfo(self,email):
        result = person.getPersonInfo(email)
        self.user_fname.text = "First Name: " + result[0]
        self.user_lname.text = "Last Name: " + result[1]
        self.user_email.text = "Email: " + result[2]
        self.user_phone.text = "Phone Number: " + result[3]
        self.user_addr.text = "Home Address: " + result[4]

    def getClientAccountInfo(self):
        if (self.client_email.text == ""):
            pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Please fill in email field."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
            return -1
        elif (self.client_email.text.find("@") == -1 or self.client_email.text.find(".") == -1):
            pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Please use a valid email."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
            return -1
        else:
            result = person.getPersonInfo(self.client_email.text)
            if (result != -1):
                self.client_fname.text = "First Name: " + result[0]
                self.client_lname.text = "Last Name: " + result[1]
                self.client_demail.text = "Email: " + result[2]
                self.client_phone.text = "Phone Number: " + result[3]
                self.client_addr.text = "Home Address: " + result[4]
                self.client_usertype.text = "User Type: " + result[5]
                return 0
            else:
                pop = Popup(title = "Admin Control Panel",
                        content = Label(text="ERROR: Cannot display this user's info."),
                        size_hint=(None,None), size=(400,200))
                pop.open()
                return -1
        
    def moveToClient(self):
        if (self.client_email.text == ""):
            pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Please fill in email field."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
            return -1
        elif (self.client_email.text.find("@") == -1 or self.client_email.text.find(".") == -1):
            pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Please use a valid email."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
            return -1
        else:
            userType = person.checkUserType(self.client_email.text)
            if (userType != "person"):
                pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Cannot move this user into client"),
                    size_hint=(None,None), size=(400,200))
                pop.open()
            elif (client.createClient(self.client_email.text) != -1):
                pop = Popup(title = "Admin Control Panel",
                    content = Label(text="Client creation was successful"),
                    size_hint=(None,None), size=(400,200))
                pop.open()
                self.client_email.text = ""
            else:
                pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Something went wrong when moving user to client"),
                    size_hint=(None,None), size=(400,200))
            pop.open()

    def removeClient(self):
        if (self.client_email.text == ""):
            pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Please fill in email field."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
            return -1
        elif (self.client_email.text.find("@") == -1 or self.client_email.text.find(".") == -1):
            pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Please use a valid email."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
            return -1
        else:
            userType = person.checkUserType(self.client_email.text)
            print("User type for client is: ", userType)
            if (userType != "member" and userType != "client"):
                pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Cannot remove this user from client"),
                    size_hint=(None,None), size=(400,200))
                pop.open()
            elif (client.removeClient(self.client_email.text) != -1):
                pop = Popup(title = "Admin Control Panel",
                    content = Label(text="Client removal was successful"),
                    size_hint=(None,None), size=(400,200))
                pop.open()
                self.client_email.text = ""
            else:
                pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Something went wrong when removing from client"),
                    size_hint=(None,None), size=(400,200))
            pop.open()

    
    def moveToMember(self):
        if (self.client_email.text == ""):
            pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Please fill in email field."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
            return -1
        elif (self.client_email.text.find("@") == -1 or self.client_email.text.find(".") == -1):
            pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Please use a valid email."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
            return -1
        else:
            userType = person.checkUserType(self.client_email.text)
            if (userType != "client"):
                pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Cannot move this user into member"),
                    size_hint=(None,None), size=(400,200))
                pop.open()
            elif (member.createMember(self.client_email.text) != -1):
                pop = Popup(title = "Admin Control Panel",
                    content = Label(text="Member creation was successful"),
                    size_hint=(None,None), size=(400,200))
                pop.open()
                self.client_email.text = ""
            else:
                pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Something went wrong when moving user to member"),
                    size_hint=(None,None), size=(400,200))
            pop.open()

    
    def removeMember(self):
        if (self.client_email.text == ""):
            pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Please fill in email field."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
            return -1
        elif (self.client_email.text.find("@") == -1 or self.client_email.text.find(".") == -1):
            pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Please use a valid email."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
            return -1
        else:
            userType = person.checkUserType(self.client_email.text)
            # print("User type for client is: ", userType)
            if (userType != "member"):
                pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Cannot remove this user from member"),
                    size_hint=(None,None), size=(400,200))
                pop.open()
            elif (member.removeMember(self.client_email.text) != -1):
                pop = Popup(title = "Admin Control Panel",
                    content = Label(text="Member removal was successful"),
                    size_hint=(None,None), size=(400,200))
                pop.open()
                self.client_email.text = ""
            else:
                pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Something went wrong when removing from member"),
                    size_hint=(None,None), size=(400,200))
            pop.open()


    def moveToEmployee(self):
        if (self.client_email.text == ""):
            pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Please fill in email field."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
            return -1
        elif (self.client_email.text.find("@") == -1 or self.client_email.text.find(".") == -1):
            pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Please use a valid email."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
            return -1
        else:
            userType = person.checkUserType(self.client_email.text)
            if (userType == "owner" or userType == "admin"):
                pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Cannot move this user into employee"),
                    size_hint=(None,None), size=(400,200))
                pop.open()
            elif (employee.createEmployee(self.client_email.text) != -1):
                pop = Popup(title = "Admin Control Panel",
                    content = Label(text="Employee creation was successful"),
                    size_hint=(None,None), size=(400,200))
                pop.open()
                self.client_email.text = ""
            else:
                pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Something went wrong when moving user to employee"),
                    size_hint=(None,None), size=(400,200))
            pop.open()

    def removeEmployee(self):
        if (self.client_email.text == ""):
            pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Please fill in email field."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
            return -1
        elif (self.client_email.text.find("@") == -1 or self.client_email.text.find(".") == -1):
            pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Please use a valid email."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
            return -1
        else:
            userType = person.checkUserType(self.client_email.text)
            # print("User type for client is: ", userType)
            if (userType != "ruser"):
                pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Cannot remove this user from employee"),
                    size_hint=(None,None), size=(400,200))
                pop.open()
            elif (employee.removeEmployee(self.client_email.text) != -1):
                pop = Popup(title = "Admin Control Panel",
                    content = Label(text="Employee removal was successful"),
                    size_hint=(None,None), size=(400,200))
                pop.open()
                self.client_email.text = ""
            else:
                pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Something went wrong when removing from employee"),
                    size_hint=(None,None), size=(400,200))
            pop.open()


    def moveToAdmin(self):
        if (self.client_email.text == ""):
            pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Please fill in email field."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
            return -1
        elif (self.client_email.text.find("@") == -1 or self.client_email.text.find(".") == -1):
            pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Please use a valid email."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
            return -1
        else:
            userType = person.checkUserType(self.client_email.text)
            print(userType)
            if (userType != "person"):
                pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Cannot move this user into manager"),
                    size_hint=(None,None), size=(400,200))
                pop.open()
            elif (manager.createManager(self.client_email.text) != -1):
                pop = Popup(title = "Admin Control Panel",
                    content = Label(text="Manager creation was successful"),
                    size_hint=(None,None), size=(400,200))
                pop.open()
                self.client_email.text = ""
            else:
                pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Something went wrong when moving user to manager"),
                    size_hint=(None,None), size=(400,200))
            pop.open()

    def removeAdmin(self):
        if (self.client_email.text == ""):
            pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Please fill in email field."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
            return -1
        elif (self.client_email.text.find("@") == -1 or self.client_email.text.find(".") == -1):
            pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Please use a valid email."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
            return -1
        else:
            userType = person.checkUserType(self.client_email.text)
            # print("User type for client is: ", userType)
            if (userType != "admin"):
                pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Cannot remove this user from manager"),
                    size_hint=(None,None), size=(400,200))
                pop.open()
            elif (manager.removeManager(self.client_email.text) != -1):
                pop = Popup(title = "Admin Control Panel",
                    content = Label(text="Manager removal was successful"),
                    size_hint=(None,None), size=(400,200))
                pop.open()
                self.client_email.text = ""
            else:
                pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Something went wrong when removing from manager"),
                    size_hint=(None,None), size=(400,200))
            pop.open()

    def getClasses(self):
        headers = ["date","time","email","fname","lname"]
        result = [dict(zip(headers, data)) for data in classes.getAllClasses()]
        return result

    def getSupplies(self):
        headers = ["supplyname","supplyno","stock"]
        result = [dict(zip(headers, data)) for data in supplies.getAllSupplies()]
        # print(result)
        return result

    def getEquip(self):
        headers = ["equipno","cdn","branchno"]
        result = [dict(zip(headers, data)) for data in equipment.getAllEquipment()]
        return result

    def getRooms(self):
        headers = ["roomid","date","duration"]
        result = [dict(zip(headers, data)) for data in rooms.getAllRooms()]
        # print(result)
        return result

    def getScheduleInfo(self):
        headers = ["timeslot","name","email"]
        results = [dict(zip(headers, data)) for data in schedule.getSchedule("Sunday")]
        self.schedulesun.data = [{'label_1': str(x['timeslot']), 'label_2': str(x['name']), 'label_3': str(x['email'])} for x in results]
        results = [dict(zip(headers, data)) for data in schedule.getSchedule("Monday")]
        self.schedulemon.data = [{'label_1': str(x['timeslot']), 'label_2': str(x['name']), 'label_3': str(x['email'])} for x in results]
        results = [dict(zip(headers, data)) for data in schedule.getSchedule("Tuesday")]
        self.scheduletues.data = [{'label_1': str(x['timeslot']), 'label_2': str(x['name']), 'label_3': str(x['email'])} for x in results]
        results = [dict(zip(headers, data)) for data in schedule.getSchedule("Wednesday")]
        self.schedulewed.data = [{'label_1': str(x['timeslot']), 'label_2': str(x['name']), 'label_3': str(x['email'])} for x in results]
        results = [dict(zip(headers, data)) for data in schedule.getSchedule("Thursday")]
        self.schedulethurs.data = [{'label_1': str(x['timeslot']), 'label_2': str(x['name']), 'label_3': str(x['email'])} for x in results]
        results = [dict(zip(headers, data)) for data in schedule.getSchedule("Friday")]
        self.schedulefri.data = [{'label_1': str(x['timeslot']), 'label_2': str(x['name']), 'label_3': str(x['email'])} for x in results]
        results = [dict(zip(headers, data)) for data in schedule.getSchedule("Saturday")]
        self.schedulesat.data = [{'label_1': str(x['timeslot']), 'label_2': str(x['name']), 'label_3': str(x['email'])} for x in results]

    def modifyBooking(self):
        popup = ModifyBookingPopup()
        popup.open()

    def modifyEquip(self):
        popup = ModifyEquipmentPopup()
        popup.open()

    def modifySchedule(self):
        popup = ModifySchedulePopup()
        popup.open()

    def logout(self):
        global loggedInEmail
        loggedInEmail = None






class EmpHomepage(Screen):
    client_email = ObjectProperty(None)
    client_fname = ObjectProperty(None)
    client_lname = ObjectProperty(None)
    client_demail = ObjectProperty(None)
    client_phone = ObjectProperty(None)
    client_addr = ObjectProperty(None)
    user_fname = ObjectProperty(None)
    user_lname = ObjectProperty(None)
    user_email = ObjectProperty(None)
    user_phone = ObjectProperty(None)
    user_addr = ObjectProperty(None)
    pass 

    def __init__(self, **kwargs):
        super(EmpHomepage, self).__init__(**kwargs)
        # print(array)
        # self.accountInfo.data = 
        self.classes.data = [{'label_1': str(x['date']), 'label_2': str(x['time']), 'label_3': str(x['email']), 'label_4': x['fname'], 'label_5': x['lname']} for x in self.getClasses()]
        self.supplies.data = [{'label_1': str(x['supplyno']), 'label_2': str(x['supplyname']), 'label_3': str(x['stock'])} for x in self.getSupplies()]
        self.equipment.data = [{'label_1': str(x['equipno']), 'label_2': str(x['cdn']), 'label_3': str(x['branchno'])} for x in self.getEquip()]
        self.rooms.data = [{'label_1': str(x['roomid']), 'label_2': str(x['date']), 'label_3': str(x['duration'])} for x in self.getRooms()]
        # self.getScheduleInfo()
        self.getScheduleInfo()
        # print(self.supplies.data)

    def on_enter(self):
        self.getCurrentAccountInfo(loggedInEmail)
    

    def getCurrentAccountInfo(self,email):
        result = person.getPersonInfo(email)
        self.user_fname.text = "First Name: " + result[0]
        self.user_lname.text = "Last Name: " + result[1]
        self.user_email.text = "Email: " + result[2]
        self.user_phone.text = "Phone Number: " + result[3]
        self.user_addr.text = "Home Address: " + result[4]


    def getClasses(self):
        headers = ["date","time","email","fname","lname"]
        result = [dict(zip(headers, data)) for data in classes.getAllClasses()]
        return result

    def getSupplies(self):
        headers = ["supplyname","supplyno","stock"]
        result = [dict(zip(headers, data)) for data in supplies.getAllSupplies()]
        # print(result)
        return result

    def getEquip(self):
        headers = ["equipno","cdn","branchno"]
        result = [dict(zip(headers, data)) for data in equipment.getAllEquipment()]
        return result

    def getRooms(self):
        headers = ["roomid","date","duration"]
        result = [dict(zip(headers, data)) for data in rooms.getAllRooms()]
        # print(result)
        return result

    def getScheduleInfo(self):
        headers = ["timeslot","name","email"]
        results = [dict(zip(headers, data)) for data in schedule.getSchedule("Sunday")]
        self.schedulesun.data = [{'label_1': str(x['timeslot']), 'label_2': str(x['name']), 'label_3': str(x['email'])} for x in results]
        results = [dict(zip(headers, data)) for data in schedule.getSchedule("Monday")]
        self.schedulemon.data = [{'label_1': str(x['timeslot']), 'label_2': str(x['name']), 'label_3': str(x['email'])} for x in results]
        results = [dict(zip(headers, data)) for data in schedule.getSchedule("Tuesday")]
        self.scheduletues.data = [{'label_1': str(x['timeslot']), 'label_2': str(x['name']), 'label_3': str(x['email'])} for x in results]
        results = [dict(zip(headers, data)) for data in schedule.getSchedule("Wednesday")]
        self.schedulewed.data = [{'label_1': str(x['timeslot']), 'label_2': str(x['name']), 'label_3': str(x['email'])} for x in results]
        results = [dict(zip(headers, data)) for data in schedule.getSchedule("Thursday")]
        self.schedulethurs.data = [{'label_1': str(x['timeslot']), 'label_2': str(x['name']), 'label_3': str(x['email'])} for x in results]
        results = [dict(zip(headers, data)) for data in schedule.getSchedule("Friday")]
        self.schedulefri.data = [{'label_1': str(x['timeslot']), 'label_2': str(x['name']), 'label_3': str(x['email'])} for x in results]
        results = [dict(zip(headers, data)) for data in schedule.getSchedule("Saturday")]
        self.schedulesat.data = [{'label_1': str(x['timeslot']), 'label_2': str(x['name']), 'label_3': str(x['email'])} for x in results]

    # def getSchedule(self):

    def getClientAccountInfo(self):
        if (self.client_email.text == ""):
            pop = Popup(title = "Member Control Panel",
                    content = Label(text="ERROR: Please fill in email field."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
            return -1
        elif (self.client_email.text.find("@") == -1 or self.client_email.text.find(".") == -1):
            pop = Popup(title = "Member Control Panel",
                    content = Label(text="ERROR: Please use a valid email."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
            return -1
        else:
            userType = person.checkUserType(self.client_email.text)
            if (userType == "member" or userType == "client" or userType == "person"):
                result = person.getPersonInfo(self.client_email.text)
                if (result != -1):
                    self.client_fname.text = "First Name: " + result[0]
                    self.client_lname.text = "Last Name: " + result[1]
                    self.client_demail.text = "Email: " + result[2]
                    self.client_phone.text = "Phone Number: " + result[3]
                    self.client_addr.text = "Home Address: " + result[4]
                    return 0
                else:
                    pop = Popup(title = "Member Control Panel",
                        content = Label(text="ERROR: Cannot display this user's info."),
                        size_hint=(None,None), size=(400,200))
                    pop.open()
                    return -1
            else:
                pop = Popup(title = "Member Control Panel",
                        content = Label(text="ERROR: Cannot display this user's info."),
                        size_hint=(None,None), size=(400,200))
                pop.open()
                return -1

    def moveToClient(self):
        if (self.client_email.text == ""):
            pop = Popup(title = "Member Control Panel",
                    content = Label(text="ERROR: Please fill in email field."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
            return -1
        elif (self.client_email.text.find("@") == -1 or self.client_email.text.find(".") == -1):
            pop = Popup(title = "Member Control Panel",
                    content = Label(text="ERROR: Please use a valid email."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
            return -1
        else:
            userType = person.checkUserType(self.client_email.text)
            if (userType != "person"):
                pop = Popup(title = "Member Control Panel",
                    content = Label(text="ERROR: Cannot move this user into client"),
                    size_hint=(None,None), size=(400,200))
                pop.open()
            elif (client.createClient(self.client_email.text) != -1):
                pop = Popup(title = "Member Control Panel",
                    content = Label(text="Client creation was successful"),
                    size_hint=(None,None), size=(400,200))
                pop.open()
                self.client_email.text = ""
            else:
                pop = Popup(title = "Member Control Panel",
                    content = Label(text="ERROR: Something went wrong when moving user to client"),
                    size_hint=(None,None), size=(400,200))
            pop.open()


    def removeClient(self):
        if (self.client_email.text == ""):
            pop = Popup(title = "Member Control Panel",
                    content = Label(text="ERROR: Please fill in email field."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
            return -1
        elif (self.client_email.text.find("@") == -1 or self.client_email.text.find(".") == -1):
            pop = Popup(title = "Member Control Panel",
                    content = Label(text="ERROR: Please use a valid email."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
            return -1
        else:
            userType = person.checkUserType(self.client_email.text)
            print("User type for client is: ", userType)
            if (userType != "member" and userType != "client"):
                pop = Popup(title = "Member Control Panel",
                    content = Label(text="ERROR: Cannot remove this user from client"),
                    size_hint=(None,None), size=(400,200))
                pop.open()
            elif (client.removeClient(self.client_email.text) != -1):
                pop = Popup(title = "Member Control Panel",
                    content = Label(text="Client removal was successful"),
                    size_hint=(None,None), size=(400,200))
                pop.open()
                self.client_email.text = ""
            else:
                pop = Popup(title = "Member Control Panel",
                    content = Label(text="ERROR: Something went wrong when removing from client"),
                    size_hint=(None,None), size=(400,200))
            pop.open()

    
    def moveToMember(self):
        userType = person.checkUserType(self.client_email.text)
        if (self.client_email.text == ""):
            pop = Popup(title = "Member Control Panel",
                    content = Label(text="ERROR: Please fill in email field."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
            return -1
        elif (self.client_email.text.find("@") == -1 or self.client_email.text.find(".") == -1):
            pop = Popup(title = "Member Control Panel",
                    content = Label(text="ERROR: Please use a valid email."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
            return -1
        else:
            userType = person.checkUserType(self.client_email.text)
            if (userType != "client"):
                pop = Popup(title = "Member Control Panel",
                    content = Label(text="ERROR: Cannot move this user into member"),
                    size_hint=(None,None), size=(400,200))
                pop.open()
            elif (member.createMember(self.client_email.text) != -1):
                pop = Popup(title = "Member Control Panel",
                    content = Label(text="Member creation was successful"),
                    size_hint=(None,None), size=(400,200))
                pop.open()
                self.client_email.text = ""
            else:
                pop = Popup(title = "Member Control Panel",
                    content = Label(text="ERROR: Something went wrong when moving user to member"),
                    size_hint=(None,None), size=(400,200))
            pop.open()

    
    def removeMember(self):
        if (self.client_email.text == ""):
            pop = Popup(title = "Member Control Panel",
                    content = Label(text="ERROR: Please fill in email field."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
            return -1
        elif (self.client_email.text.find("@") == -1 or self.client_email.text.find(".") == -1):
            pop = Popup(title = "Member Control Panel",
                    content = Label(text="ERROR: Please use a valid email."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
            return -1
        else:
            userType = person.checkUserType(self.client_email.text)
            # print("User type for client is: ", userType)
            if (userType != "member"):
                pop = Popup(title = "Member Control Panel",
                    content = Label(text="ERROR: Cannot remove this user from member"),
                    size_hint=(None,None), size=(400,200))
                pop.open()
            elif (member.removeMember(self.client_email.text) != -1):
                pop = Popup(title = "Member Control Panel",
                    content = Label(text="Member removal was successful"),
                    size_hint=(None,None), size=(400,200))
                pop.open()
                self.client_email.text = ""
            else:
                pop = Popup(title = "Member Control Panel",
                    content = Label(text="ERROR: Something went wrong when removing from member"),
                    size_hint=(None,None), size=(400,200))
            pop.open()

    def modifyBooking(self):
        popup = ModifyBookingPopup()
        popup.open()

    def modifyEquip(self):
        popup = ModifyEquipmentPopup()
        popup.open()
            
        
        
    def logout(self):
        global loggedInEmail
        loggedInEmail = None



#------------------------------------------------ CLIENT HOMEPAGE -------------------------------------------------------------------------------------------------#

class ClientHomepage(Screen):
    user_fname = ObjectProperty(None)
    user_lname = ObjectProperty(None)
    user_email = ObjectProperty(None)
    user_phone = ObjectProperty(None)
    user_addr = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(ClientHomepage, self).__init__(**kwargs)

        self.classes.data = [{'label_1': str(x['date']), 'label_2': str(x['time']), 'label_3': str(x['email']), 'label_4': x['fname'], 'label_5': x['lname']} for x in self.getClasses()]
    pass

    def on_enter(self):
        self.getCurrentAccountInfo(loggedInEmail)

    def getCurrentAccountInfo(self,email):
        headers = ['fname','lname','email','phone','address']
        result = person.getPersonInfo(email)
        self.user_fname.text = "First Name: " + result[0]
        self.user_lname.text = "Last Name: " + result[1]
        self.user_email.text = "Email: " + result[2]
        self.user_phone.text = "Phone Number: " + result[3]
        self.user_addr.text = "Home Address: " + result[4]

    def getClasses(self):
        headers = ["date","time","email","fname", "lname"]
        result = [dict(zip(headers, data)) for data in classes.getAllClasses()]
        return result
    
    def logout(self):
        global loggedInEmail
        loggedInEmail = None


Builder.load_file("pagemanager.kv")

sm = ScreenManager()
sm.add_widget(LoginForm(name="login"))
sm.add_widget(RegForm(name="registration"))
sm.add_widget(ClientHomepage(name="chomepage"))
sm.add_widget(EmpHomepage(name="ehomepage"))
sm.add_widget(AdminHomepage(name="ahomepage"))

class MainApp(App):
    def build(self):
        return sm

if __name__ == "__main__":
    MainApp().run()
    #GYM CLASS NEEDED
    db.close()