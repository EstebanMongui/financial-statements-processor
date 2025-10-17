# Importar librerías
import regex as re

from FileManager import FileManager
from processor import FinancialStatementsProcessor
from statement import StatementFile
from processor import Processor

# Todo: this should be received as parameter
date_pattern = r"[0-9]+[A-Za-z]{3}[0-9]+ +([A-Z]+ )+ +\$"
fm = FileManager()


class TxtExpensesProcessor(FinancialStatementsProcessor, Processor):
    def __init__(self, data_structure):
        super().__init__()
        self.data_structure = data_structure

    def get_header(self, file, data_structure):
        head_line = ""
        print("data_structure: ", data_structure) # TODO: remove
        for line in file:
            if "Fecha" in line and "Valor a" in line:
                # FIXME: write code to detect the head of the expenses table
                head_line = line
        return head_line

    def clean_movements(self, movements):
        spaces_pattern = r" {2,}"
        enter_pattern = r"\n"
        cleaned_movements = []
        for movement in movements:
            _expense = re.sub(spaces_pattern, "|", movement)
            _expense = re.sub(enter_pattern, "", _expense)
            cleaned_movements.append(_expense.split("|"))

        for movement in cleaned_movements:
            del movement[4:]
            movement.pop(0)

        return cleaned_movements 
    
    def get_movements_by_file(self, file_path):
        @fm.read_file(file_path)
        def get_movements(file):
            movements = []
            for line in file:
                if re.search(self.data_structure['pattern'], line):
                    movements.append(line)
            return movements

        return get_movements()
    
    def get_movements(self):
        all_movements = []
        for statement_file in self.statement_files:
            movements = self.get_movements_by_file(statement_file.file_path)
            all_movements.extend(movements)
        return all_movements 

    def process(self):
        movements = self.get_movements()
        cleaned_movements = self.clean_movements(movements)
        return cleaned_movements


if __name__ == "__main__":
    data_structure = {
        "pattern": date_pattern,
    }

    file = StatementFile("txt", "./data/", "julio")

    processor = TxtExpensesProcessor(data_structure)
    processor.statements_files = [file]
    movements = processor.process()
    print(movements)
