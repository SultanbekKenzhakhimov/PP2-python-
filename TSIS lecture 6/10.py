def even(l):
    evennum = list()
    for i in range(len(l)):
        l[i] = int(l[i])
        if l[i] % 2 == 0:
            evennum.append(l[i])
    return even
nums = input().split()
print(evennum(nums))