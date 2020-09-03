from collections import OrderedDict

def check_item(key):
    try:
        _dict[key] = 1 + _dict.setdefault(key)
    except:
        _dict[key] = 1

_dict = OrderedDict()
s = list(map(str, [i for i in input()]))
for i in s:
    check_item(i)

new_list = sorted(_dict.items(), key=lambda t: t[1], reverse=True)
for i in range(3):
    print('{} {}'.format(new_list[i][0], new_list[i][1]))