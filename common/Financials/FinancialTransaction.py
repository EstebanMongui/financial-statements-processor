from abc import ABC, abstractmethod

from common import Transaction
from common.Financials import Currency

class FinancialTransaction(ABC,Transaction): 
    @property
    @abstractmethod
    def currency(self) -> Currency:
        pass

    @property
    @abstractmethod
    def amount(self) -> float:
        pass