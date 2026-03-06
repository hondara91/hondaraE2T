import random
import string

password = ""
char = string.digits

for i in range(2): 
    password += random.choice(char)

print (password)

for i in range(3):
    usernum = input("INTRODUCE EL NÚMERO: ")
    if int(usernum) == int(password): 
        print ("Well done")
        break
    elif int(usernum) < int(password): print ("Sube un poco campeón")
    elif int(usernum) > int(password): print ("Bájale")

if int(usernum) != int(password): print("Nahhhh... se te acabaron las oportunidades, muy mal")
else: print("FELICIDADES")
