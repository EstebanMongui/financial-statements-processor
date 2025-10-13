from typing import Literal
from abc import ABC, abstractmethod

FileTypes = Literal['txt', 'csv', 'pdf', 'xlsx']

class File(ABC):
    @abstractmethod
    @property
    def type(self) -> FileTypes:
        pass

    @abstractmethod
    @property
    def name(self) -> str:
        pass

    @abstractmethod
    @property
    def path(self) -> str:
        pass

    @abstractmethod
    @property
    def password(self) -> str:
        pass