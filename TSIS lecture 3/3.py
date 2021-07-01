line = input()
words = line.split(' ')
numbers = [int(i) for i in words]
numbers.reverse()
print(numbers)