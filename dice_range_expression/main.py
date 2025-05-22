with open('./input.txt', 'r') as f:
  input = [[abs(int(_)) for _ in i.strip().split()] for i in f.readlines()]
dices = [20, 10, 8, 6, 4, 3, 2]

used_all = []
for i in input:
  used = ""
  for j in i:
    _ = 0
    while _ < len(dices) and j > 0:
      if j >= dices[_]:
        if f"{dices[_]}" not in used:
          if used != "":
            used += f"+d{dices[_]}-{abs((i[0] + i[1]) - (dices[_] + int(used.replace("d", ""))))}"
          else: used += f"d{dices[_]}"
          j -= dices[_]
        else: break
      _ += 1
  used_all.append(used)

input = ""
for i in used_all:
  input += f"{i}\n"
print(input.strip())