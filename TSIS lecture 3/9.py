n = int(input())
m = int(input())
s1 = set()
s2 = set()
for i in range(n):
    x = int(input())
    s1.add(x)
for i in range(m):
    x = int(input())
    s2.add(x)
s3 = set()
s3 = s2.intersection(s1)
s4 = s1.difference(s2)
s5 = s2.difference(s1)
print(len(s3) , s3 , ";" , len(s4) , s4 ,";", len(s5) , s5)
