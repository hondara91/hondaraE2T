import random
import string


password = ""
char = string.ascii_letters + string.digits + string.ascii_uppercase

for i in range(10): 
    password += random.choice(char)

print (password)
