from typing import Literal
from abc import ABC, abstractmethod

FileTypes = Literal['txt', 'csv', 'pdf', 'xlsx']

class File(ABC):
    @property
    @abstractmethod
    def type(self) -> FileTypes:
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass

    @property
    @abstractmethod
    def path(self) -> str:
        pass

    @property
    @abstractmethod
    def password(self) -> str:
        pass

    @property
    @abstractmethod
    def is_encrypted(self) -> bool:
        pass

    @property
    def file_path(self):
        path = self.path

        if not self.path.endswith("/"):
            path += "/"

        return path + self.name + "." + self.type