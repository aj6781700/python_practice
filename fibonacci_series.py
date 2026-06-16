fib=[0,6]
#range starts from 0 buy derfault
n=5
for i in range(n):
  fib.append(fib[-1]+fib[-2])
  #converting the list of integers to string
  print(', '.join(str(e) for e in fib))