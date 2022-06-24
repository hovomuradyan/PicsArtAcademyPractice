l1 = []
k = input("Input word: ")
l1.append(k)
while k != '':
    k = input("Input word: ")
    if not k in l1:
        l1.append(k)
l1.pop()
print(l1)
