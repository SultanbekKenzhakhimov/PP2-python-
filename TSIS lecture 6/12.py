def isPalin(string):
    if string == stirng[::-1] :
        return "is a palindrome"
    else:
        return "is not a palindrome"
s = input()
print(isPalin(s))