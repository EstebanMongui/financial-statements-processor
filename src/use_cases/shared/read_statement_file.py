#Responsibility:
## Reads the file content and metadata

class ReadStatementFile:
    #TODO: define FileReader interface
    def __init__(self, file_reader):
        self.file_reader = file_reader
    
    def read(self, file_path):
        return self.file_reader.read(file_path)