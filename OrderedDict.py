from collections import OrderedDict

_dict = OrderedDict()

N = int(input())

def add_item(name, price):
    try:
       _dict[name] = price + _dict.setdefault(name)
    except:
        _dict[name] = price

for _ in range(N):
    *itemName, netPrice = input().split()
    name = ' '.join(itemName)
    price = int(netPrice)
    add_item(name, price)

for k, v in _dict.items():
    print('{} {}'.format(k, v))