with open('./input.txt', 'r') as f:
  input = [[int(_) for _ in i.strip().split()] for i in f.readlines()]

print(input)
