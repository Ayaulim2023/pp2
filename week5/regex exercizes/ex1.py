import re

file = 'abbbcdab ab a abc'
result = re.findall("ab*", file)

print(result)