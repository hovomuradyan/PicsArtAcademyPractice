def funt_to_sm(a):
  return a / 0.032808

def dm_to_sm(a):
        return a * 2.54

ft = int(input("Please , input your height ft: "))
dm = int(input("Please , input your height dm: "))
total_height = funt_to_sm(ft) + dm_to_sm(dm)
print("Your height in sm is " , total_height)
