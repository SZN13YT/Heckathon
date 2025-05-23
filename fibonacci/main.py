with open('./input.txt', 'r') as f:
  input = f.read()

input = input.strip().split()
def fibonacci(n):
  if n == 0 or n == 1: return n
  elif 0 <= n <= int(i): return fibonacci(n-1) + fibonacci(n-2)
  print(n)
for i in input:
  if i.isnumeric():
    print(fibonacci(10))
  print()
print(input)
