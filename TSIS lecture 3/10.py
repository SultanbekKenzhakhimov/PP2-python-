n = int(input())
dictionary = {}
for i in range(n):
    key , syn = input().split()
    dictionary[key] = syn
    dictionary[syn] = key
print(dictionary[input()])