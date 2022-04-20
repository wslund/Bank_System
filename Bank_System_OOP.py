

class User:

    def __init__(self, first_name: str, last_name: str, amount: float, currency):
        self.first_name = first_name
        self.last_name = last_name
        self.amount = amount
        self.currency = currency

    def insert_money(self, insert):
        insert = insert
        self.amount += insert
        return



    def __str__(self):
        return f'{self.first_name}-{self.last_name} {self.amount} {self.currency}'



class Bank:
    def __init__(self, name):
        self.name = name
        self.bankaccount = {}

    def create_bankaccount(self, user):
        first_name = user.first_name
        last_name = user.last_name
        user_name = f'{first_name}-{last_name}'
        self.bankaccount[user_name] = user
        return


    def search_customer(self, first_name, last_name):
        first_name = first_name
        last_name = last_name
        user_name = f'{first_name}-{last_name}'
        customers = [i for i in self.bankaccount]

        for i in customers:
            if user_name not in customers:
                return print('Sorry could not find User')
            else:
                return print(f'Found: {self.bankaccount[user_name]}')


    def __str__(self):
        return f'{self.name} - {self.bankaccount}'



user1 = User(first_name='FirstName1', last_name='LastName1', amount=100, currency='$')
user2 = User(first_name='FirstName2', last_name='LastName2', amount=50, currency='$')
print(user1)
print(user2)
#------------------------------------------------------------------------------------------


bank1 = Bank(name='Bank1')
print(bank1)
#------------------------------------------------------------------------------------------


bank1.create_bankaccount(user1)
bank1.create_bankaccount(user2)
print(bank1)
#------------------------------------------------------------------------------------------


bank1.search_customer(first_name='FirstName1', last_name='LastName1')

# When the user is not present.
bank1.search_customer(first_name='Wrong', last_name='user')
#------------------------------------------------------------------------------------------


user1.insert_money(insert=300)
print(bank1.search_customer(first_name='FirstName1', last_name='LastName1'))
