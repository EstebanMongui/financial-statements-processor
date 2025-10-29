from abc import ABC, abstractmethod

class Currency(ABC):
    @property
    @abstractmethod
    def code(self) -> str:
        pass
    
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def symbol(self) -> str:
        pass

    @property
    @abstractmethod
    def rate(self) -> float:
        pass

    @property
    @abstractmethod
    def decimals(self) -> int:
        pass

    @property
    @abstractmethod
    def format(self) -> str:
        pass

    @property
    @abstractmethod
    def associated_countries(self) -> List[Country]:
        pass