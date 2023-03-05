import re

file = 'abbbcdab ab a abc abb sdabbhj'
result = re.findall("ab{2,3}", file)

print(result)