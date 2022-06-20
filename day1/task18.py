s1 = int(input("Input the first side: "))
s2 = int(input("Input the second side: "))
s3 = int(input("Input the third side: "))
s = (s1 + s2 + s3) / 2
area = math.sqrt(s * (s-s1) * (s-s2) * (s-s3))
print("Area is" , area)
