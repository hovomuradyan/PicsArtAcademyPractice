pi = math.pi
def area_of_circle(a):
  return pow(pi*r, 2)

r = int(input("Input circle radius: "))
h = int(input("Input circle height: "))
print(round(area_of_circle * h , 1))
