from abc import ABC, abstractmethod
from common import Subject

class Transferer(ABC,Subject):
    # Who made the transfer
    @property
    @abstractmethod
    def type(self) -> SUBJECT_TYPES:
        pass