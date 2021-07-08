def check(n, x, y):
    if x <= n <= y:
        return "The input number is in range"
    else:
        return "The input number is not in range"
n = int(input())
x = int(input())
y = int(input())
print(check(n, x, y))