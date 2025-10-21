from abc import ABC, abstractmethod
from typing import Union, Literal 

FINANCIAL_TRANSACTION_TYPE_NAME= Literal['income', 'expense']
FINANCIAL_TRANSACTION_SYMBOLS = Literal['+', '-']

class FinancialTransactionType(ABC):
    @property
    @abstractmethod
    def name(self) -> Union[FINANCIAL_TRANSACTION_TYPE_NAME]:
        pass

    @property
    @abstractmethod
    def symbol(self) -> Union[FINANCIAL_TRANSACTION_SYMBOLS]:
        pass