from datetime import *

class Event:
    
    def __init__(self, startTime, endTime, venue):
        self.startTime = startTime
        self.endTime = endTime
        self.venue = venue
    
    def getDescription(self):
        return f"Event start time: {self.startTime}, end time: {self.endTime}, venue: {self.venue.getDescription()}"
        
class Venue:
    
    def __init__(self, name, address):
        self.name = name
        self.address = address
        
    def getDescription(self):
        return f"Venue name: {self.name}, address: {self.address.getDescription()}"

class Address:
    
    def __init__(self, street, city, state, country, zipcode):
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.zipcode = zipcode

    def getDescription(self):
        return f"Address street: {self.street}, city: {self.city}, state: {self.state}, country: {self.country}, zipcode: {self.zipcode}"

address = Address("via Martiri della Libertà 64", "Vasto", "Chieti", "Italy", "66054")
venue = Venue("Teatro Rossetti", address)

d = date(2024, 12, 1)
startTime = time(19)
endTime = time(20)
event = Event(datetime.combine(d, startTime), datetime.combine(d, endTime), venue)

print(event.getDescription())
