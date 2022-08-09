import re

nomer = input('Enter nomer: ')
pattern = r'^0'
nam = '+996'
result = re.sub(pattern, nam, nomer)
print(result)