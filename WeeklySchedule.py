from connection import *
from Employee import *
from datetime import date
import random

class WeeklySchedule:
    def __init__(self, database):
        self.db = database
        self.days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday', 'Saturday']
        today = date.today()
        self.week_no = today.isocalendar().week
        self.timeSlots = ['6-10', '10-2', '2-6', '6-12']
        # i = 0
        # max = employees.size()
        # array = []
        # for row in self.days:
        #     times = []
        #     for index in self.timeSlots:
        #         times.append(employees[i])
        #         i = i + 1
        #         if(i>max):
        #             i = 0
            
        #array.append(times)
        
        self.schedule = array
        
        
    def getWeek(self):
        return self.week_no
    
    def getTimeSlots(self):
        return self.timeSlots
    
    def getDays(self):
        return self.days
    
    def getSchedule(self, day):
        return getWeeklySchedule(day) #will return an array of time slots for one day
    
    def getEmployees(self):
        return self.db.getEmployees()
    
        
