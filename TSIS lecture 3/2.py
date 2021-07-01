line = input()
words = line.split(' ')
numbers = [int(i) for i in words]
positive = []
for i in range(len(numbers)):
    if(numbers[i] > 0):
        positive.append(numbers[i])
min = positive[0]
for i in range(len(positive)):
    if(positive[i] < min):
        min = positive[i]
print(min)