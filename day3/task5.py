def clear_string(s1):
    s2 = ""
    for a in s1:
        if (a.isalpha()) == True or a == " ":
            s2+=a.lower()
    return s2

def reversed_string(x):
    s1 = ""
    l1 = x.split()
    l1 = l1[::-1]
    for i in l1:
        s1+=i
        s1+=" "
    return s1
    

def is_polindrom(s1):
    if(clear_string(s1) + " " == reversed_string(clear_string(s1))):
        return True
    else:
        return False
        
s1 = input("Please , input your string: ")
print(is_polindrom(s1))
