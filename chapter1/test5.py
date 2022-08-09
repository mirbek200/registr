import re

pattern = r"/\w.+"
text = ' localhost:8888/ilovepython/lihkujhku/iuiuh'
result = re.search(pattern , text)
print(result.group())