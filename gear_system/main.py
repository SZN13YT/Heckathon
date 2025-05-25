with open('./input.txt', 'r') as f:
  input = f.read()

lines = []
for i in input.strip().split("\n"):
  line = [[]]
  for j in range(len(i)):
    if i[j].isnumeric(): line[0].append(int(i[j]))
    elif i[j] == "]": break
  try: line.append(int(i[j+2]))
  except: line.append(8)
  lines.append(line)

def fugg(l, n=8): 
  base = [3, 3 ,3]
  if l == base:
    return [0, 0, 0]
  
  m = [0, 0, 0]
  if l[0] < base[0]:
    base[0] = l[0]
    base[1] = l[0]
    m[0] += l[0]
    m[1] += l[0]
  if l[2] < base[2]:
    base[2] += l[2]
    base[1] += l[2]
    m[1] += l[2]
    m[2] += l[2]
  for i in range(len(base)):
    if base[i] > 3:
      base[i] -= 3
  if base == l and m[1] <= n:
    return m
    


for i in lines:
  megold = fugg(i[0], i[1])
  try:
    for j in range(megold[0]):print("left", end=" ")
    for j in range(megold[2]):print("right",end=" ")
    print()
  except: print("Megoldhatatlan")
