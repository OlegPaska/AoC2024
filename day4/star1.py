lines = []
with open("in.txt", 'r') as f:
  lines = f.read().splitlines()

count = 0

#this took 1.5 hours :sob:
#horizontal
for y in range(len(lines)):
  for x in range(len(lines[0])-3):
    if lines[y][x:x+4] == "XMAS": count+=1
    if lines[y][x:x+4] == "SAMX": count+=1

#vertical
for y in range(len(lines)-3):
  for x in range(len(lines[0])):
    aggv = ""
    for i in range(4):
      aggv += lines[y+i][x]
    if aggv == "XMAS": count+=1
    if aggv == "SAMX": count+=1

#diagonal right
for y in range(len(lines)-3):
  for x in range(len(lines[0])-3):
    aggdr = ""
    for i in range(4):
      aggdr += lines[y+i][x+i]
    if aggdr == "XMAS": count+=1
    if aggdr == "SAMX": count+=1

#diagonal left
for y in range(len(lines)-3):
  for x in range(3,len(lines[0])):
    aggdl = ""
    for i in range(4):
      aggdl += lines[y+i][x-i]
      #print(y+i, x-i)
    if aggdl == "SAMX": count+=1
    if aggdl == "XMAS": count+=1
print(count)

