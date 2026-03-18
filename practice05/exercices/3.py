#Write a Python program to find sequences of lowercase letters joined with a underscore.

txt = input()
import re
result = re.findall(r'[a-z]+_[a-z]+', txt)
print(result)