import random
import string 

def random_passwd(n):
    s = ""
    for i in range(num):
        s+=random.choice(string.ascii_lowercase)
    return s
    
num = int(input("Input your password lenght: "))
print(random_passwd(num))
