def check_safe(line):
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
  return safe

def check_safe_list(line):
  safe = True
  diff = int(line[0]) - int(line[1])
  
  if abs(diff) <1 or abs(diff) > 3:
    safe = False

  diff2 = 0
  for i in range(1,len(line)-1):
    if diff * (int(line[i]) - int(line[i+1])) < 0:
      safe = False
      break
    diff = diff2
    diff2 = int(line[i]) - int(line[i+1])
    if diff * diff2 < 0:
      safe = False
      break
    if abs(diff2) < 1 or abs(diff2) > 3:
      safe = False
      break
  return safe

f = open("in.txt", 'r')
safe_count = 0

#hackiest solution ever lolll i was desperate to finish this before uni
for line in f:
  if check_safe(line):
    safe_count += 1
  else:
    nums = line.split()
    safe = False
    for i in range(len(nums)):
      numbs = list(nums)
      numbs.pop(i)
      if check_safe_list(numbs):
        safe = True
    if safe: safe_count+=1
print(safe_count)

