import glob
c_list = list()
f_list = glob.glob("*.txt")
for f_element in f_list:
   with open(f_element , "r") as file:
       c_list.append(file.read())
print(c_list)