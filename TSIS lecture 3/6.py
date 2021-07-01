line = input()
words = line.split(' ')
numbers = [int(i) for i in words]
s = set(numbers)
print(len(s))