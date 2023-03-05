import re

txt = "PythonExerCizes"

result = re.sub(r"(\w)([A-Z])", r"\1 \2", txt)

print(result)