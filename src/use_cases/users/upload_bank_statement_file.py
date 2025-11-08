#Responsibilities:
#1. Allows user to upload one or more files to the system

from interfaces import FileUploader

class UploadBankStatementFile:
    def __init__(self, file_uploader: FileUploader):
        self.file_uploader = file_uploader

    def upload(self, file_path):
        self.file_uploader.upload(file_path);