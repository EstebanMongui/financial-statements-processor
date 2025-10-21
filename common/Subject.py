from abc import ABC, abstractmethod

class Subject(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def address(self) -> str:
        pass