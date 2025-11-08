from abc import ABC, abstractmethod

class FileUploader(ABC):
    @property
    @abstractmethod
    def uploaded_file_metadata(self):
        pass

    @property
    @abstractmethod
    def file(self):
        pass

    @abstractmethod
    def upload(self, file_path):
        pass

    @abstractmethod
    def get_uploaded_file_metadata(self):
        pass

    @abstractmethod
    def get_file(self):
        pass
