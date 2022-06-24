def reversed_string(s1):
    s2 = ""
    for i in range(len(s1)):
        s2+=s1[len(s1)-1 - i]
    return s2

inputed_string = input("Please , input your string")
print(reversed_string(inputed_string))
