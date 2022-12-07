from datetime import date

class WeeklySchedule:
    def __init__(self, database):
        self.db = database
        self.days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday','Friday', 'Saturday']

        self.timeSlots = ['6-10', '10-2', '2-6', '6-12']
        
    
    
    def getTimeSlots(self):
        return self.timeSlots
    
    def getDays(self):
        return self.days
    
    def getSchedule(self, day):
        results = self.db.getWeeklySchedule(day) #will return an array of time slots for one day
        return results

