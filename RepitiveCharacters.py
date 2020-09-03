import re

pattern = r'(\d+|[a-z]+)\1+'
m = re.search(pattern, input())
if m:
    print(m.group(0)[:1])
else:
    print('-1')