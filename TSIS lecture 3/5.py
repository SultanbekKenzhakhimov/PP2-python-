line = input()
words = line.split(' ')
numbers = [int(i) for i in words]
k = int(input())
print(*numbers[-k:], end=' ')
print(*numbers[0:-k])