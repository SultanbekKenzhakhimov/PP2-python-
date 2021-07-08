def isPrime(num):
    counter = 0
    for i in range(2 , num + 1):
        if num % i == 0:
            counter = counter + 1
    if counter == 1:
        return "The input number is prime"
    else:
        return "The input number is not prime"
num = int(input())
if (num < 2) :
    print("Please choose positive number, that is higher than 2 ")
else:
    print(isPrime(num))