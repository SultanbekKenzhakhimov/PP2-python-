with open('скриптонит.txt', "w", encoding='utf8') as file:
    file.write("Hello\n")
    file.write('Test text')
x = open('скриптонит.txt') 
print(x.read())