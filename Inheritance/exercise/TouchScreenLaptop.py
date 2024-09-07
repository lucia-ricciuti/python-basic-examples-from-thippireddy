from abc import abstractmethod, ABC

class TouchScreenLaptop(ABC):
    
    @abstractmethod
    def scroll(self):
        pass
    
    @abstractmethod
    def click(self):
        pass

class HP(TouchScreenLaptop):    
    
    def scroll(self):
        print("HP Scrolling")
        
class Dell(TouchScreenLaptop):

    def scroll(self):
        print("Dell Scrolling")

class HPNotebook(HP):
    
    def click(self):
        print("HPNotebook clicking")
    
    def scroll(self):
        super().scroll()
        print("Also HPNotebook clicking")

class DellNotebook(Dell):
    
    def click(self):
        print("DellNotebook clicking")
        
hpNotebook = HPNotebook()
hpNotebook.scroll()
hpNotebook.click()

dellNotebook = DellNotebook()
dellNotebook.click()
dellNotebook.scroll()

    