def isPang(string):
    temp = ''
    for i in range(len(s)):
        if string[i].isalnum():
            temp = temp + s[i]
    l = set()
    for i in range(len(temp)):
        l.add(temp[i])
    if (len(l) > 25) :
        return "The input string is pangram"
    else:
        return "The input string is not pangram"
string = input().lower()
print(isPang(string))