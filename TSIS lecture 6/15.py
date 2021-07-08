def hyp(string):
    x = sorted(string)
    print(*x , sep = '-')
hyp(input().split('-'))