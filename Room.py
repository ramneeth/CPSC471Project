from ConnectionGUI import *

class Room:
    def __init__(self, database):
        self.db = database

    def getAllRooms(self):
        results = self.db.getRoomInfo()
        return results

    def addBooking(self, roomid, date, duration):
        results = self.db.addBooking(roomid,date,duration)
        return results

    def removeBooking(self, roomid, date, duration):
        results = self.db.removeBooking(roomid,date,duration)
        return results