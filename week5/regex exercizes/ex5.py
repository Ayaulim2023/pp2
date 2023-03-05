import re

file = 'setrdtfabvcvb  aab cab'
result = re.findall(".*a.+b$", file)

print(result)