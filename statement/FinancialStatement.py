from abc import ABC

class FinancialStatement(ABC):
    def __init__(self):
        super().__init__()
        self.__file_path = '' 
    
    @property
    def file_path(self):
        return self.__file_path
    
    @file_path.setter
    def file_path(self, file_path):
        self.__file_path = file_path
        return self