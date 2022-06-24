def is_prime(n):
  for i in range(2,n):
    if (n%i) == 0:
      return False
  return True

def smallest_prime(num):
    num+=1
    while is_prime(num) != True:
        num+=1
    return num
    
num = int(input("Please , input your number: "))
print(smallest_prime(num))
