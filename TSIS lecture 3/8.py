line = input()
words = line.split(' ')
numbers1 = [int(i) for i in words]
line2 = input()
words2 = line2.split(' ')
numbers2 = [int(i) for i in words2]
s1 = set(numbers1)
s2 = set(numbers2)
s3 = set()
s3 = s2.intersection(s1)
print(s3)