import re

pattern = r".+w.+"
text = """wonderful,
owner     
"""
res = re.search(pattern, text)
if res:
    print('Match!')
    print(res.group())
else:
    print('Not a match!')