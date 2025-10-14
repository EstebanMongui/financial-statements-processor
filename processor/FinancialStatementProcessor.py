from abc import ABC, abstractmethod

class FinancialStatementsProcessor(ABC):
    @property
    @abstractmethod
    def statements_files(self):
        pass

    @abstractmethod
    def get_header(self, file, data_structure):
        pass

    @abstractmethod
    def get_movements(self, data_structure):
        pass

    @abstractmethod
    def clean_movements(self, movements):
        pass

    def process(self):
        pass