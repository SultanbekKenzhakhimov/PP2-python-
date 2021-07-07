with open('скриптонит.txt', encoding='utf8') as file:
    x = [next(file) for i in range(int(input()))]
print(*x)