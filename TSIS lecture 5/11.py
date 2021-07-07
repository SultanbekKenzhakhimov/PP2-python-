import os
info = os.stat('скриптонит.txt')
print(info.st_size, 'bytes')