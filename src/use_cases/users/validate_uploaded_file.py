'''
Responsibility: Validates file properties
    - File size
    - File extension
    - File content
'''

class ValidateUploadedFile:
    #TODO: define FileValidator interface
    def __init__(self, file_validator, validation_rules):
        self.file_validator = file_validator
        self.validation_rules = validation_rules

    def validate(self, file_metadata):
        self.file_validator.validate(file_metadata, self.validation_rules)

        
        