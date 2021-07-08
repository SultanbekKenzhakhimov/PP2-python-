def unique_list(l):
    unique_l = list()
    for i in l:
        if i not in unique_l:
            unique_l.append(i)
        else:
            continue
    return unique_l
l = input().split()
print(unique_list(l))