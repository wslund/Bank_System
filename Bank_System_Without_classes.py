
Bank = {}
Users = {}


def create_bank(name):
    bank_profile = {
        'accounts': {}
    }
    Bank[name] = bank_profile
    return Bank



def create_user(first_name, last_name, amount, currency):
    user_name = first_name + '-' + last_name
    Users[user_name] = {'first_name': first_name, 'last_name': last_name, 'amount': amount, 'currency': currency}
    return Users


def user_to_bank(name):
    Bank[name]['accounts'] = Users
    return Bank

def search_customer(bankName,first_name, last_name):
    user_name = first_name + '-' + last_name
    while True:
        bank = Bank[bankName]['accounts']
        if user_name not in bank:
            return print('Sorry could not find')

        else:
            first_name = Bank[bankName]['accounts'][user_name]['first_name']
            last_name = Bank[bankName]['accounts'][user_name]['last_name']
            amount = Bank[bankName]['accounts'][user_name]['amount']
            currency = Bank[bankName]['accounts'][user_name]['currency']
            return print(f'{first_name} {last_name} {amount} - {currency}')


def insert_money(bankName, first_name, last_name, insert):
    user_name = first_name + '-' + last_name
    while True:
        bank = Bank[bankName]['accounts']
        if user_name not in bank:
            return print('Sorry could not find Customer')
        else:
            ammo = insert
            ammo = float(ammo)
            amount = Bank[bankName]['accounts'][user_name]['amount']
            usr_dict = Bank[bankName]['accounts'][user_name]
            update = amount + ammo
            usr_dict.update({'amount': update})
            amount_view = Bank[bankName]['accounts'][user_name]['amount']
            currency_view = Bank[bankName]['accounts'][user_name]['currency']
            return print(f'Tank you, your amount is now: {amount_view} {currency_view}')




bank1 = create_bank(name='bank1')


#----------------------------------------------------------------------------


user1 = create_user(first_name='firstName1', last_name='lastName1', amount=100, currency='$')
user2 = create_user(first_name='firstName2', last_name='lastName2', amount=0, currency='$')
user3 = create_user(first_name='firstName3', last_name='lastName3', amount=1000, currency='$')
#-----------------------------------------------------------------------------


user_to_bank(name='bank1')
#-----------------------------------------------------------------------------


print('Search Customer:')
search_customer(bankName='bank1', first_name='firstName1', last_name='lastName1')
print('----------------------------------')

#-----------------------------------------------------------------------------


print('Before: Insert Money')

search_customer(bankName='bank1', first_name='firstName1', last_name='lastName1')
print('----------------------------------')
print('After: Insert Money')
insert_money(bankName='bank1', first_name='firstName1',last_name='lastName1', insert=200)
print('----------------------------------')
#-----------------------------------------------------------------------------










