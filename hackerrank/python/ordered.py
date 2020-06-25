from collections import OrderedDict

size = int(input())
orders = OrderedDict() 

for i in range(size):
    order = input().split()
    price = order[-1]
    name = ' '.join(order[:-1])

    if name in orders.keys():
        orders[name] += int(price)
    else:
        orders[name] = int(price)

for key, value in orders.items():
    print ('{} {}'.format(key, value))