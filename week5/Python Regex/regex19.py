import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object

x1 = re.search(r"\bS\w+", txt)
print(x1.span())

x2 = re.search(r"\bS\w+", txt)
print(x2.string)

x3 = re.search(r"\bS\w+", txt)
print(x3.group())