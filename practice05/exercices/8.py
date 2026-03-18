#Write a Python program to split a string at uppercase letters.

txt = input()
import re
result = re.split(r'(?=[A-Z])', txt)
print(result)