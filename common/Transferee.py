from abc import ABC, abstractmethod
from common import Subject
from common import SUBJECT_TYPES

class Transferee(ABC,Subject):
    # Who received the transfer
    @property
    @abstractmethod
    def type(self) -> SUBJECT_TYPES:
        pass