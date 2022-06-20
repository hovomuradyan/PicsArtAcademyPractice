def ft_to_dm(a):
  return ft * 12

def ft_to_ml(a):
  return 1 * 0.000189394

def ft_yrd(a):
  return 1 * 0.333333

num = int(input("Input number in ft: "))
print("FT to DM", ft_to_dm(num))
print("FT to ML", ft_to_ml(num))
print("FT to YRD", ft_to_yrd(num))
