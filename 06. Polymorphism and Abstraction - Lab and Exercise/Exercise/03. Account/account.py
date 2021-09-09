class Account:
    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def add_transaction(self, amount):

        if type(amount) != int:
            raise ValueError("please use int for amount")
        self._transactions.append(amount)

    @property
    def balance(self):
        return f"{sum(self._transactions) + self.amount}"

    # we must use a static method (няма self или cls)
    @staticmethod
    def validate_transaction(account, amount_to_add):
        if account.balance + amount_to_add < 0:
            raise ValueError("sorry cannot go in debt!")
        account.add_transaction(amount_to_add)
        return f"New balance: {account.balance}"

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, item):
        for i in range(len(self._transactions)):
            return self._transactions[item]

    def __ge__(self, other):
        if sum(self._transactions) >= sum(other._transactions):
            return True
        return False

    def __gt__(self, other):
        if sum(self._transactions) > sum(other._transactions):
            return True
        return False

    def __eq__(self, other):
        if sum(self._transactions) == sum(other._transactions):
            return True
        return False

    def __add__(self, other):
        result = Account(f"{self.owner}&{other.owner}", self.amount + other.amount)
        result._transactions = self._transactions + other._transactions
        return result

acc = Account('bob', 10)
acc2 = Account('john')
print(acc)
print(repr(acc))
acc.add_transaction(20)
acc.add_transaction(-20)
acc.add_transaction(30)
print(acc.balance)
print(len(acc))
for transaction in acc:
    print(transaction)
print(acc[1])
print(list(reversed(acc)))
acc2.add_transaction(10)
acc2.add_transaction(60)
print(acc > acc2)
print(acc >= acc2)
print(acc < acc2)
print(acc <= acc2)
print(acc == acc2)
print(acc != acc2)
acc3 = acc + acc2
print(acc3)
print(acc3._transactions)