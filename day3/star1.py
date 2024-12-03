import re
f = open("in.txt", 'r')

#wowee regex
total = 0
for line in f:
  muls = re.findall("mul\(\d+,\d+\)", line)
  for mul in muls:
    d = re.findall("\d+", mul)
    total += int(d[0]) * int(d[1])
print(total)