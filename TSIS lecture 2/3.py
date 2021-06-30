line = input()
words = line.split(' ')
numbers = [int(i) for i in words]
counter = 0
for i in range(0 , len(numbers)):
    for j in range(i + 1 , len(numbers)):
        if(numbers[i] == numbers[j]):
            counter = counter + 1
print(counter)

