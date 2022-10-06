from os import system
from bdlogo import logo
clear = lambda: system('cls')

logo()

log = [
    {
        'names': [],
        'money': [],
    },
]

Flag = True

while Flag:
    name = input('Enter your name: ')
    bid_price = int(input('Enter your bid price: '))
    log[0]['names'].append(name)
    log[0]['money'].append(bid_price)
    go = input('There are other users to bid (y/n) ')

    max_bid = max(log[0]['money'])
    max_bid_index = log[0]['money'].index(max_bid)
    winner = log[0]['names'][max_bid_index]

    if go == 'y':
        Flag = True
        clear()
    else:
        Flag = False
        print(f"You are the highest bidder {winner}")
