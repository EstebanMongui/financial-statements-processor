class Expense:
    __init__(self):
        self.__id = None
        self.__date = None
        self.__concept = None
        self.__amount = None
        self.__currency = None
        self.__payment_method = None

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, expense_date):
        if(not isinstance(expense_date, date)):
            raise TypeError('The introduced date doesnt have a valid datetime format')
        if(expense_date > date.now()):
            raise ValueError('An expense date cannot be greater than the current date')

        self.__date = expense_date
        return self

    @property
    def id(self):
        return __id

    def __generate_id(self):
        random_id = 'This should be implemented' #Todo: implement the function to generate a random id
        self.__id = random_id

    @property
    def concept(self):
        return self.__concept

    @concept.setter
    def setConcept(self, concept: string):
        self.__concept = concept
        return self

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def setAmount(self, amount):
        self.__amount = amount
        return self

    @property
