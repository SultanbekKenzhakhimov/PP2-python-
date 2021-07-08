def counter_case(string):
    counterlow = 0
    counterup = 0
    for i in string :
        if i.isupper():
            counterup = counterup + 1
        if i.islower():
            counterlow = counterlow + 1
    return counterup , counterlow
s = input()
print(counter_case(s))