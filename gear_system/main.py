with open('./input.txt', 'r') as f:
  input = f.read()
print(input.strip().split("\n"))

lines = []
for i in input.strip().split("\n"):
  line = []
  for j in i:
    if j.isnumeric(): line.append(int(j))
  lines.append(line)

def fugg(l, n=8):
  levers = {
    "left" : [1, 1, 0],
    "right" : [0, 1, 1]
  }
  
  eredmeny = "Megoldhatatlan"
  for i in range(n):
    pass
  return eredmeny


for i in lines:
  try:
    fugg([i[0], i[1], i[2]], i[3])
  except: 
      fugg([i[0], i[1], i[2]])