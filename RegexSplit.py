import re
pattern = r'[,.]'
print('\n'.join(re.split(pattern, input())))