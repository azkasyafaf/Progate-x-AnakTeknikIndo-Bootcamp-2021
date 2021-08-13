from atm_card import ATMCard

class Costumer(ATMCard):
    def __init__(self, id, custPin = 1234, custBalance = 10000):
        self.id = id
        super().__init__(custPin, custBalance)
        """self.pin = custPin
        self.balance = custBalance"""
    
    def checkID(self):
        return self.id
    """
    def checkPin(self):
        return self.pin

    def checkBalance(self):
        return self.balance
    """
    def withdraw(self, nominal):
        self.balance -= nominal

    def deposit(self, nominal):
        self.balance += nominal