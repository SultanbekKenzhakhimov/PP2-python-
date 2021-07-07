import string , os
if not os.path.exists("letters"):
   os.makedirs("letters")
for letter in s.ascii_upper:
   with open(l + ".txt", "w") as file:
       file.writelines(l)