# account = {
#     'checking': 1980,
#     'savings' : 2800
# }
#
# def add_money(amount: float, name: str = 'checking') -> float:
#     account[name] += amount
#
# add_money(900)
# print(account['checking'])
# add_money(220, 'savings')
# print(account)

def create_account(name: str, holder: str, account_holders: list = []):
    account_holders.append(holder)
    return {
        'name': name,
        'holder': holder,
        'account_holders': account_holders

    }

a1 = create_account('checking', 'Rolf')
a2 = create_account('savings', 'Jen')

# how to avoid mutable argument problems
#will return by default 2 holders - how to solve - don't pass default argument
# pass default argument as None, then []

#1 don't pass argument list default
def create_account(name: str, holder: str, account_holders):
    account_holders.append(holder)
    return {
        'name': name,
        'holder': holder,
        'account_holders': account_holders

    }

b1 = create_account('checking', 'Rolf', [])
b2 = create_account('savings', 'Jen', [])


#2 make it none
def create_account(name: str, holder: str, account_holders: None):
    if not account_holders:
        account_holders = []

    account_holders.append(holder)
    return {
        'name': name,
        'holder': holder,
        'account_holders': account_holders

    }

b1 = create_account('checking', 'Rolf', ['Ola'])
b2 = create_account('savings', 'Jen', [])

print(b1)
print(b2)