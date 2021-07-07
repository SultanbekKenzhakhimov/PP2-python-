import re
print(*filter(None, re.split(r'[.,]+', input())), sep='\n')