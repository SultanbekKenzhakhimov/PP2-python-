def isPerfect(num):
    d = list()
    for i in range(1, num):
        if num % i == 0:
            d.append(i)
    if (num == sum(d)):
        return "The input number is perfect number"
    else:
        return "The input number is not perfect number"
num = int(input())
print(isPerfect(num))