with open('скриптонит.txt', encoding='utf8') as file:
    x = file.read().split()
print(max(x , key = len))