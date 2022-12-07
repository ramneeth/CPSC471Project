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
        
    def booked(id, date, duration):
        canBook = notBooked(id, date)
        if(canBook == True):
            createRoom(id, date, duration)
        #else:
            #print message here
    
    def cancelBooking(id, date, duration):
        cancelBooking(id, date, duration)