import re

pattern = r".+w.+"
text = """The quick brown fox jumps over the lazy dog.
Python Exercises.    
"""
res = re.match(pattern, text)
if res:
    print('Match!')
    print(res.group())
else:
    print('Not a match!')