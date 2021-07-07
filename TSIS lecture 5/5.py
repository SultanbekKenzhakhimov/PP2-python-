n = int(input())
with open('скриптонит.txt', encoding='utf8') as file:
    x = [next(file) for i in range(n)]
print(x)