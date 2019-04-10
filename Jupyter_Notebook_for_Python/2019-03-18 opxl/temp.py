import re
k = "aa"
regul = re.finditer(r'(?=('+k+'))','aaadaa')

for i in regul:
    print(i.start(1), i.end())
    