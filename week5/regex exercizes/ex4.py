import re

file = 'Abbbcdab Ab a ABc'
result = re.findall("[A-Z]{1}[a-z]+", file)

print(result)