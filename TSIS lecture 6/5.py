def facts(n):
    m = 1
    for i in range(1, n + 1):
        m = m * i
    return m
n = int(input())
print(facts(n))