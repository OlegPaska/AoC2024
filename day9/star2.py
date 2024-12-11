inp = []
with open("in.txt") as f:
    inp = list(f.readline())
for i in range(len(inp)):
    inp[i]= int(inp[i])
disk = []
ID = 0
flip = True
gaps = []
files = []
for i in range(len(inp)):
    if flip:
        for j in range(inp[i]):
          disk.append(ID)
        ID+=1
        files.append(inp[i])
    else:
        for j in range(inp[i]):
          disk.append('.')
        gaps.append(inp[i])
    flip = not flip

print(disk)


def recalculate():
  fc = 0
  gc = 0
  gaps.clear()
  files.clear()
  last = disk[0]
  for i in disk:
    if (last == '.') != (i == '.'):
      if i == '.':
        gaps.append(gc)
        gc = 0
      else:
        files.append(fc)
        fc = 0
    if i == '.':
      gc +=1
    else:
      fc +=1
    last = i
  gaps.pop(0)
  files.append(fc)
  gaps.append(gc)

    


#edge case HELLLL
# gaps.append(0)
# filled = [0]*len(range(len(files)))
# for i in range(len(files)-1, -1, -1):
#   for j in range(len(gaps)):
#     if files[i] <= gaps[j] and files[i] !=0:
#       gapIndex = sum(inp[:j*2+1])
#       fileIndex = sum(inp[:i*2])
#       temp = disk[gapIndex:gapIndex+files[i]]
#       disk[gapIndex:gapIndex+files[i]] = disk[fileIndex:fileIndex+files[i]]
#       disk[fileIndex:fileIndex+files[i]] = temp
#       gaps[j] -= files[i]
#       gaps[i] += files[i]
#       files[i] = 0
#       files[j] += files[i]
#       #recalculate()
#       print(disk)
#       break

for i in range(len(files)-1, -1, -1):
  count = 0
  fileIndex = sum(inp[:i*2])
  for j in range(fileIndex):
    if disk[j] == '.':
      count+=1
      if count >= files[i]:
        
        j +=1
        temp = disk[j-count:j]
        disk[j-count:j] = disk[fileIndex:fileIndex+files[i]]
        disk[fileIndex:fileIndex+files[i]] = temp
        print(disk)
        break
    else:
      count = 0

s=0
for i in range(len(disk)):
    if disk[i] != '.': s+=i*disk[i]
print(s)




