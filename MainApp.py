import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout
from ConnectionGUI import Database

db = Database()
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
                    db.createPerson(self.ssn.text, self.fname.text, self.lname.text, 
                                    self.addr.text, self.passw.text, self.phone.text, self.email.text)
                    print("Name: ", self.fname.text, self.lname.text)
                    print("Email: ", self.email.text)
                    print("Address: ", self.addr.text)
                    print("Phone Number: ", self.phone.text)
                    print("SSN: ", self.ssn.text)
                    print("Password: ",self.passw.text)
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


class AdminHomepage(Screen):
    admin_email = ObjectProperty(None)
    #tempClass = [["01/23/2022","9:50","0","test@gmail.com","John Smith"], ["01/24/2022","9:50","0","test2@gmail.com","Jalal Kawash"]]
    pass 

    def moveToAdmin(self):
        if (self.admin_email.text == ""):
            pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Please fill in email field."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
            return -1
        elif (self.admin_email.text.find("@") == -1 or self.admin_email.text.find(".") == -1):
            pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Please use a valid email."),
                    size_hint=(None,None), size=(400,200))
            pop.open()
            return -1
        else:
            if (db.createAdmin(self.admin_email.text) != -1):
                pop = Popup(title = "Admin Control Panel",
                    content = Label(text="Admin creation was successful"),
                    size_hint=(None,None), size=(400,200))
                pop.open()
            else:
                pop = Popup(title = "Admin Control Panel",
                    content = Label(text="ERROR: Something went wrong when moving user to admin"),
                    size_hint=(None,None), size=(400,200))
            pop.open()
        
    def logout(self):
        global loggedInEmail
        loggedInEmail = None


class ClientHomepage(Screen):

    tempClass = [["01/23/2022","9:50","0","test@gmail.com","John Smith"], ["01/24/2022","9:50","0","test2@gmail.com","Jalal Kawash"]]

    # tempClass = [{'date': '01/23/2022', 'time': '9:50', 'branchno': '0', 'email': 'test@gmail.com', 'tname':'John Smith'},
    #          {'date': '01/24/2022', 'time': '12:30', 'branchno': '0', 'email': 'test2@gmail.com', 'tname':'Jalal Kawash'},
    #          {'date': '01/25/2022', 'time': '9:50', 'branchno': '0', 'email': 'test3@gmail.com', 'tname':'Jane Smith'},
    #          {'date': '01/26/2022', 'time': '16:00', 'branchno': '0', 'email': 'test4@gmail.com', 'tname':'Kawhi Leonard'}
    #         ]

    # tempEquip = [{'equipno': '01', 'amount': '30', 'condition': 'Good', 'branchno': '0'},
    #          {'equipno': '02', 'amount': '25', 'condition': 'Maintenance', 'branchno': '0'},
    #          {'equipno': '03', 'amount': '122', 'condition': 'Good', 'branchno': '0'},
    #          {'equipno': '04', 'amount': '33', 'condition': 'Maintenance', 'branchno': '0'}
    #         ]

    def __init__(self, **kwargs):
        super(ClientHomepage, self).__init__(**kwargs)

        self.classes.data = [{'label_1': str(x['date']), 'label_2': str(x['time']), 'label_3': str(x['email']), 'label_4': x['fname'], 'label_5': x['lname']} for x in self.getClasses()]
        # self.equipment.data = [{'label_1':str(x['equipno']), 'label_2': str(x['amount']), 'label_3': str(x['condition']), 'label_4': x['branchno']} for x in self.tempEquip]

    pass

    def getClasses(self):
        headers = ["date","time","email","fname", "lname"]
        result = [dict(zip(headers, data)) for data in db.getClassInfo()]
        return result
    
    def logout(self):
        global loggedInEmail
        loggedInEmail = None



class EmpHomepage(Screen):
    client_email = ObjectProperty(None)
    tempClass = [["01/23/2022","9:50","0","test@gmail.com","John Smith"], ["01/24/2022","9:50","0","test2@gmail.com","Jalal Kawash"]]
    pass 

    def __init__(self, **kwargs):
        super(EmpHomepage, self).__init__(**kwargs)
        array = self.getClasses()
        # print(array)
        # self.accountInfo.data = 
        self.classes.data = [{'label_1': str(x['date']), 'label_2': str(x['time']), 'label_3': str(x['branchno']), 'label_4': x['email'], 'label_5': x['tname']} for x in self.getClasses()]

    def getClasses(self):
        headers = ["date","time","branchno","email","tname"]
        result = [dict(zip(headers, data)) for data in self.tempClass]
        return result

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
            if (db.createClient(self.client_email.text) != -1):
                pop = Popup(title = "Member Control Panel",
                    content = Label(text="Client creation was successful"),
                    size_hint=(None,None), size=(400,200))
                pop.open()
            else:
                pop = Popup(title = "Member Control Panel",
                    content = Label(text="ERROR: Something went wrong when moving user to client"),
                    size_hint=(None,None), size=(400,200))
            pop.open()
        
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
    db.close()