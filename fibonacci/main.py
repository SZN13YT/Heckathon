with open('./input.txt', 'r') as f:
  input = f.read()

input = input.strip().split()
def fibonacci(n):
  b = 0
  next = 1
  back = ""
  while 0 <= b <= n:
    if b % 3 == 0: back += f"{b} "
    a, b = b, next
    next = a + b
  return back.strip().split()
for i in input:
  try:
    fibo = fibonacci(int(i))
    if len(fibo) > 0:
      for _ in range(len(fibo)):
        if _ < len(fibo) -1: print(fibo[_], end=", ")
        else: print(fibo[_])
    else: print("N/A")
  except: print("N/A")