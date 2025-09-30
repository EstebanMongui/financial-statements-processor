# Importar librerías
import pandas as pd
import regex as re

from FileManager import FileManager

# Todo: this should be received as parameter
date_pattern = r"[0-9]+[A-Za-z]{3}[0-9]+ +([A-Z]+ )+ +\$"
fm = FileManager()


class ExpensesProcessor:
    def __init__(self, file_path, file_name):
        self.__file_path = file_path
        self.__file_name = file_name
        self.expenses = None

    def get_header(file):
        head_line = ""
        for line in file:
            if "Fecha" in line and "Valor a" in line:
                # TOFIX: write code to detect the head of the expenses table
                head_line = line
        return head_line

    def file_path(self):
        return self.__file_path

    @fm.read_file(file_path)
    def __get_expense_lines(file):
        expenses = []

        for line in file:
            if re.search(date_pattern, line):
                expenses.append(line)

        return expenses

    def __parse_expenses(expenses):
        # Clean the expenses detected
        spaces_pattern = r" {2,}"
        enter_pattern = r"\n"
        expense_records = []
        for expense in expenses:
            _expense = re.sub(spaces_pattern, "|", expense)
            _expense = re.sub(enter_pattern, "", _expense)
            expense_records.append(_expense.split("|"))

        for record in expense_records:
            del record[4:]
            record.pop(0)

        return expense_records

    def generate_expenses(self):
        expense_lines = self.__get_expense_lines()
        expenses = self.__parse_expenses(expense_lines)

        return expenses


if __name__ == "__main__":
    file_path = ""
    file_name = ""
    processor = ExpensesProcessor(file_path, file_name)
