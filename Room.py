from ConnectionGUI import *

class Room:
    def __init__(self, database):
        self.room_id = None
        self.date = None
        self.duration = None
        self.db = database

    def getAllRooms(self):
        results = self.db.getRoomInfo()
        return results

    def addBooking(self, roomid, date, duration):
        self.room_id = roomid
        self.date = date
        self.duration = duration
        results = self.db.addBooking(roomid,date,duration)
        return results

    def removeBooking(self, roomid, date, duration):
        self.room_id = None
        self.date = None
        self.duration = None
        results = self.db.removeBooking(roomid,date,duration)
        return results