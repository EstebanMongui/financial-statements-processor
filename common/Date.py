from abc import ABC, abstractmethod

class Date(ABC):
 
    @property
    @abstractmethod
    def day(self) -> int:
        pass
    
    @property
    @abstractmethod
    def month(self):
        pass
    
    @property
    @abstractmethod
    def year(self):
       pass 
    
    @property
    @abstractmethod
    def date(self):
        pass
 
    @abstractmethod
    def create_date(self):
        pass