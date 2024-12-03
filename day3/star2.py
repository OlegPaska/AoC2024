import re
f = open("in.txt", 'r')

binarylol = False
enabled = True
total = 0
for line in f:
  chunks = re.split("(do\(\)|don't\(\))", line)
  for chunk in chunks:
    if enabled:
      muls = re.findall("mul\(\d+,\d+\)", chunk)
      for mul in muls:
        d = re.findall("\d+", mul)
        total += int(d[0]) * int(d[1])
    if chunk == "don't()":
      enabled = False
    if chunk == "do()":
      enabled = True    
print(total)