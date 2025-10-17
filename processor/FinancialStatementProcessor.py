from typing import List
from abc import ABC, abstractmethod
from common.Financials import Movement
from file import File

class Finder(ABC):
    @abstractmethod
    def __find(self):
        pass

class Cleaner(ABC):
    @abstractmethod
    def __clean(self):
        pass

class Builder(ABC):
    @abstractmethod
    def __build(self):
        pass


class Field(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def type(self) -> str:
        pass

class Header(ABC):
    @abstractmethod
    def header(self) -> List[Field]:
        pass

#TODO: define the FinancialStatementsProcessor class, responsible to find, clean and build the financial movements in a given statement files

class FinancialStatementsProcessor():
    @property
    def statement_files(self):
        return self.__statements_files         

    @statement_files.setter
    def statements_files(self, statements_files: List[File]):
        if not isinstance(statements_files, list):
            raise TypeError("statements_files must be a list of File objects")

        self.__statements_files = statements_files        
        return self