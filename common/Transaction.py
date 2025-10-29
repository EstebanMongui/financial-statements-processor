from abc import ABC, abstractmethod
from common import Date, Subject

class Transaction(ABC):
    @property
    @abstractmethod
    def id(self) -> str:
        pass

    @property
    @abstractmethod
    def type(self) -> str:
        # TODO: implement the Type of TransactionType
        pass

    @property
    @abstractmethod
    def date(self) -> Date:
        pass

    @property
    @abstractmethod
    def sender(self) -> Subject:
        pass

    @property
    @abstractmethod
    def receiver(self) -> Subject:
        pass

    @property
    @abstractmethod
    def concept(self) -> str:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass