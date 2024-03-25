def count_bits(n):
  s = n
  x = 1
  arr = [1]
  add_arr = []
  sum = 0
  bin_arr = []
  while find_max(arr) <= n:
    arr.append(2 ** x)
    x +=1

  arr.pop()
  
  arr_copy = arr.copy()
  
  while sum != n: 
    sum += find_max(arr_copy) 
    s -= find_max(arr_copy)
    add_arr.append(find_max(arr_copy))
    arr_copy.pop()
    while find_max(arr_copy) > s:
      arr_copy.pop()
  
  
  arr.sort(reverse = True)

  for i in range(0, len(arr)):
    if arr[i] == find_max(add_arr):
      add_arr.pop(0)
      bin_arr.append(1)
    else:
      bin_arr.append(0)

  integer = int("".join([str(x) for x in bin_arr]))
  return count_ones(integer)
  
    
def count_ones(n):
  count = 0
  n = str(n)
  for i in n:
    if "1" == i:
      count +=1
  return count

def find_max(arr):
  max = 0
  for i in range(len(arr)):
    if max < arr[i]:
      max = arr[i]
  return max


print(count_bits(100))
  


