from abc import ABC, abstractmethod

class Country(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def code(self) -> str:
        pass

    @property
    @abstractmethod
    def coordinates(self) -> str:
        pass