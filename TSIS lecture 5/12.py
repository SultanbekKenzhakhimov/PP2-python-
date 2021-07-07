color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('alph.txt', "w") as file:
        for c in color:
                file.write("%s\n" % c)
result = open('alph.txt')
print(result.read())