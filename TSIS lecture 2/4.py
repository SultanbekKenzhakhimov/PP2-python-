line = input()
words = line.split(' ')
numbers = [int(i) for i in words]
altitudes = []
al = 0
for i in range(len(numbers)):
    al = al + numbers[i]
    altitudes.append(al)
max = 0
for i in range(len(altitudes)):
    if(altitudes[i] > max):
        max = altitudes[i]
print(max)


