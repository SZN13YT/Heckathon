with open('./input.txt', 'r') as f:
  input = [[int(j) for j in i.strip().split()] for i in f.readlines()]
def what_dice(n1, n0, nn):
  r = {20: 0, 10: 0, 8: 0, 6: 0, 4: 0, 3: 0, 2: 0}
  n = n1 - n0 + nn
  if n in r:
    r[n] += 1
    return [r, n0 - nn]
  d = 0
  for _ in r:
    if n - _ == 0:
      d += 1
      r[_] += 1
      return [r, n0 - nn + d]
    elif n - _ > 0:
      d += 1
      r[_] += 1
      n -= _
  return [r, n0 - nn + d]

for i in input:
  pr = False
  if i[0] > 1:
    out = what_dice(i[1], i[0], 1)
  else: 
    out = what_dice(i[1], i[0], 2)
  for i in [[j for j in out[0].keys()][_] for _ in range(-1, -len(out[0])-1, -1)]:
    if out[0].get(i) != 0:
      if not pr:
        pr = True
        print(f"{out[0].get(i)}d{i}", end="")
      else: print(f"+{out[0].get(i)}d{i}", end="")
  if out[1] != 0: print(f"+{out[1]}" if out[1] > 0 else f"{out[1]}")