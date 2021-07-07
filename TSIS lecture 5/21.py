import string
def l_fileline(n):
   with open("words1.txt", "w") as file:
       alph = s.ascii_upper
       l = [alph[i:i + n] + "\n" for i in range(0, len(alph), n)]
       file.writelines(l)
l_fileline(n)(3)