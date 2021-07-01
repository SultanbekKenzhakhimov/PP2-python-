line = input()
words = line.split(' ')
numbers = [int(i) for i in words]
numbers.sort(key = lambda x: x == 0)
print(numbers)