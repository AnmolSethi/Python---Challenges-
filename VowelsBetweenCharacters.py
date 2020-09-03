import re

s = input()
pattern = r'[aeiouAEIOU]{2,}'
m = re.finditer(pattern, s)
x = list(map(lambda x: x, m))

result = []
if len(x) >= 1:
    for i in x:
        if not i.span()[0] == 0 and not i.span()[1] == len(s):
            result.append(i.group())
    print('\n'.join(result))
else:
    print('-1')