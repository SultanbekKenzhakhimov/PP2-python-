def maximum(l):
    return max(l)
numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
print(maximum(numbers))