from connection import *

class Room:
    def __init__(self, id, date, duration):
        self.id = id
        self.date = date
        self.duration = duration
        createRoom(id, date, duration)
        
    def booked(id, date, duration):
        canBook = notBooked(id, date)
        if(canBook == True):
            createRoom(id, date, duration)
        #else:
            #print message here
    
    def cancelBooking(id, date, duration):
        cancelBooking(id, date, duration)