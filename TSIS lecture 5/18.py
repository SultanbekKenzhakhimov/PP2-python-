def counter(path):
    with open(path) as file:
        d = file.read()
        d.replace("," , " ")
        return len(data.split(" "))
print(counter(path)("b.txt"))