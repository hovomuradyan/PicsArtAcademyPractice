def procent_by_year(a):
  total_sum = a + a * 4/100
  return total_sum

def print_procents_for_3_year(a):
  a = procent_by_year(a)
  print(f'Fisrt year: {a}')
  a = procent_by_year(a)
  print(f'Second year: {a}')
  a = procent_by_year(a)
  print(f'Third year: {a}') 
  
sum = int(input("Input your sum: "))
print_procents_for_3_year(sum)
