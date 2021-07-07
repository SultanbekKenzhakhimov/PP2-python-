with open('скриптонит.txt', encoding = 'utf8') as file:
    d = dict()
    x = f.read().split()
    for i in x:
        d[i] = 0
    for i in x:
        d[i] = d[i] + 1
    for i in d:
        print(f'{i}: {d[i]}')