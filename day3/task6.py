n = 1
k = int(input("Input your number: "))
sum = k
l1 = [k]
while True:
    k = input("Input your number: ")
    if k != "":
        k = int(k)
        l1.append(k)
        sum += k
        n += 1
    else:
        break
sum/=n
print("Average is", sum)
print("Lower then average")
for i in l1:
    if i < sum:
        print(i, end=" ")
print()
print("Equal average")
for i in l1:
    if i == sum:
        print(i, end=" ")
print()
print("Greeter then average")
for i in l1:
    if i > sum:
        print(i, end=" ")
