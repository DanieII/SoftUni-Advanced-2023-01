class Account:
    def __init__(self, account_id, balance, pin):
        self.balance = balance
        self.__id = account_id
        self.__pin = pin

    def get_id(self, pin):
        if pin == self.__pin:
            return self.__id
        return "Wrong pin"

    def change_pin(self, old, new):
        if old == self.__pin:
            self.__pin = new
            return "Pin changed"
        return "Wrong pin"
