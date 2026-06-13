class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # public
        self._bank = "SBI"  # protected
        self.__balance = balance  # private (name-mangled)

    # @property
    def balance(self):  # getter — read as attribute
        return f"₹{self.__balance}"

    # @balance.setter
    def balance(self, amount):  # setter — validates input
        if amount < 0:
            raise ValueError("Balance cannot be negative!")
        self.__balance = amount

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"Deposited ₹{amount}. Balance: ₹{self.__balance}"

    # def __repr__(self):
    #     return f"BankAccount({self.owner}, ₹{self.__balance})"


acc = BankAccount("Arjun", 5000)
print(acc.balance)  # 5000  getter works
# acc.balance = 7000  # setter called
print(acc.deposit(500))  # Deposited ₹500. Balance: ₹7500
