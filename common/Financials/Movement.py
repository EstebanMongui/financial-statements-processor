from abc import ABC, abstractmethod
from common import Date

class Movement(ABC):
    @property
    @abstractmethod
    def date(self) -> Date:
        pass

    @property
    @abstractmethod
    def concept(self):
        pass
    
    @property
    @abstractmethod
    def place(self):
        pass

    @property
    @abstractmethod
    def currency(self) -> str:
        pass

    @property
    @abstractmethod
    def amount(self) -> float:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass