import re

file = 'ab_b aabc ansd_sijdh'
result = re.findall("[a-z]+_[a-z]+", file)

print(result)