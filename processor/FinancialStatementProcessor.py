from abc import ABC, abstractmethod
from processor import Processor
from statement import FinancialStatement

class FinancialStatementsProcessor(ABC, FinancialStatement, Processor):
    """
      - statements_files: StatementFile[] 
      - financial_movements: FinancialMovement[] 
      - getMovement(file: StatementFile, data_structure: DataStructure): Movement
      - getMovements(data_structure: DataStructure): Movement[]
      - cleanMovements(data_structure: DataStructure): Movement[]
      - process(): FinancialStatementDataFrame
    """

    @abstractmethod
    @property
    def statements_files(self):
        pass

    @abstractmethod
    def get_header(self, file, data_structure):
        pass

    @abstractmethod
    def get_movement(self, file, data_structure):
        pass

    @abstractmethod
    def get_movements(self, data_structure):
        pass

    @abstractmethod
    def clean_movements(self, movements):
        pass

    @abstractmethod
    def process(self):
        pass