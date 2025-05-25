with open('c:/Users/nando/Desktop/Heckathon/dice_range_expression/input.txt', 'r') as f:
  input = [[int(j) for j in i.strip().split()] for i in f.readlines()]

print(input)

def what_dice(n):
  r = {20: 0, 10: 0, 8: 0, 6: 0, 4: 0, 3: 0, 2: 0}
  if n in r:
    r[n] += 1
    return r
  
  for _ in r:
    if n - _ == 0:
      r[_] += 1
      return r
    elif n - _ > 0:
      r[_] += 1
      n -= _
  return r

for i in input:
  if i[0] > 1:
    out, ch = what_dice(i[1] - i[0] + 1)
    print(out, ch)
  else: 
    out = what_dice(i[1] - i[0] + 2)
  for i in out:
    if out.get(i) != 0:
      print(f"{out.get(i)}d{i}", end="")
  print()