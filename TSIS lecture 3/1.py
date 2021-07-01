line = input()
words = line.split(' ')
numbers = [int(i) for i in words]
for i in range(len(numbers)):
    if i % 2 == 0:
        print(numbers[i])