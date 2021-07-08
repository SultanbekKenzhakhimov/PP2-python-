def mult(l):
    m = 1
    for i in range(len(l)):
        m = m * l[i]
    return m
numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
print(mult(numbers))