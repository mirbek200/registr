import re

pattern = r"\d+ \w+"

text1 = "23 street"
text2 = "42 meaning of life"

res = re.match(pattern, text2)

if res:
    print('Match!')
    print(text2)
else:
    print('Not a match!')