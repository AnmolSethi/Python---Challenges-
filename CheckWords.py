from collections import OrderedDict

def add_item(word):
    try:
        _dict[word] = 1 + _dict.setdefault(word)
    except:
        _dict[word] = 1
    
_dict = OrderedDict()

N = int(input())

for _ in range(N):
    word = input().strip()
    add_item(word)

print(len(_dict))
for key, value in _dict.items():
    print('{}'.format(value), end=' ')