from abc import abstractmethod, ABC
# Interface is a class with all abstract methods
class Bmw(ABC):
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    @abstractmethod
    def start(self):
        pass
        
    @abstractmethod
    def stop(self):
        pass
        
    @abstractmethod
    def drive(self):
        pass

class ThreeSeries(Bmw):
    
    def __init__(self,  cruiseControlEnabled, make, model, year):
        # Bmw.__init__(self, make, model, year)
        super().__init__(make, model, year)
        self.cruiseControlEnabled = cruiseControlEnabled
        
    def display(self):
        print(self.cruiseControlEnabled)
        
    def start(self):
        super().start()
        print("Button Start")
        
    def stop(self):
        print("Stopping the car")

    def drive(self):
        print("Three Series is being driven")
        
class FiveSeries(Bmw):
    
    def __init__(self,  parkingAssistEnabled, make, model, year):
        # Bmw.__init__(self, make, model, year)
        super().__init__(make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled
        
threeSeries = ThreeSeries(True, "BMW", "328i", "2018")
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)
threeSeries.start()
threeSeries.stop()
threeSeries.display()
threeSeries.drive()
