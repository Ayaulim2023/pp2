import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

x1 = re.split("\s", txt, 1)
print(x1)