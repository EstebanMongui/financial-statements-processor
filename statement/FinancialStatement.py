from file import File

class StatementFile(File):
    def __init__(self, file_type, path, name):
        super().__init__()
        self.__type = file_type
        self.__path = path
        self.__name = name
        self.__password = ""
        self.__is_encrypted = False
    
    @property
    def type(self):
        return self.__type

    @property
    def name(self):
        return self.__name
    
    @property
    def path(self):
        return self.__path
    
    @property
    def password(self):
        return self.__password
    
    @property
    def is_encrypted(self):
        return self.__is_encrypted
    
    def set_is_encrypted(self, is_encrypted):
        self.__is_encrypted = is_encrypted
        return self

    def set_password(self, password):
        self.__password = password
        return self