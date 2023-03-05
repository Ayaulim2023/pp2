import re

txt = "AyauLymKuat"

print(re.findall('[A-Z][^A-Z]*', txt))