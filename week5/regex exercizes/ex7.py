import re
ex = "ASDFGHJKL: _ZXCVBN"

resilt = ''.join(x.capitalize() or '_' for x in ex.split('_'))

print(resilt)
