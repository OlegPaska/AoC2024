f = open("in.txt", 'r')
safe_count = 0
safe = True
for line in f:
  safe = True
  diff = int(line.split()[0]) - int(line.split()[1])
  
  if abs(diff) <1 or abs(diff) > 3:
    safe = False

  diff2 = 0
  for i in range(1,len(line.split())-1):
    if diff * (int(line.split()[i]) - int(line.split()[i+1])) < 0:
      safe = False
      break
    diff = diff2
    diff2 = int(line.split()[i]) - int(line.split()[i+1])
    if diff * diff2 < 0:
      safe = False
      break
    if abs(diff2) < 1 or abs(diff2) > 3:
      safe = False
      break
  if safe:
    safe_count += 1
print(safe_count)