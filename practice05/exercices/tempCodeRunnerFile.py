
import re
txt = input()
result = re.sub(r'([A-Z])', r'_\1', txt).lower()
print(result)