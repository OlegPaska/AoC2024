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
empty=0
i=0

#use raw input to find first gap for last file
#for each insert reduce gap by file size
#index is sum of elements till the file/gap
#disk[sum(inp[:fileIndex*2])]
#disk[sum(inp[:fileIndex*2+1])]
# filled = [0]*len(range(len(files)))
# for i in range(len(files)-1, -1, -1):
#   for j in range(len(gaps)):
#     if files[i] <= gaps[j]:
#       gapIndex = sum(inp[:j*2+1])
#       fileIndex = sum(inp[:i+filled[i]*2])
#       temp = disk[gapIndex:gapIndex+files[i]]
#       disk[gapIndex:gapIndex+files[i]] = disk[fileIndex:fileIndex+files[i]]
#       disk[fileIndex:fileIndex+files[i]] = temp
#       gaps[j] -= files[i]
#       filled[j] += files[i]
#       break

back = len(disk)-1
while i > back:
    # while disk[-1] == '.':
    #     disk.pop()
    if disk[i] == '.':
      while disk[back] == ".":
        back -=1
      temp = disk[i]
      disk[i] = disk[back]
      disk[back] = temp
      #print(disk)
    i+=1
print(disk)
s=0
for i in range(len(disk)):
    s+=i*disk[i]
print(s)


print(disk)
