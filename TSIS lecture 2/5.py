n = int(input())
l = []
summ = 0
product = 1
while(n != 0):
    l.append(n % 10)
    n = n // 10
for i in range(len(l)):
    summ = summ + l[i]
    product = product * l[i]
print(product - summ)