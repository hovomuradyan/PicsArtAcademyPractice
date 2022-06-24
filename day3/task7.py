def is_getting_up(data1):
    for i in range(1, len(data1)):
        if(data1[i] < data1[i-1]):
            return False
    return True

def is_getting_low(data1):
    for i in range(1, len(data1)):
        if(data1[i] > data1[i-1]):
            return False
    return True
    
def is_progression(l1):
    if(is_getting_up(l1) or is_getting_low(l1)):
        return True
    else:
        return False    

l1 = []
while True:
    k = input("Input your number: ")
    if k != "":
        k = int(k)
        l1.append(k)
    else:
        break
print(is_progression(l1))
