inp = []
with open("in.txt") as f:
    inp = list(f.readline())
for i in range(len(inp)):
    inp[i]= int(inp[i])
disk = []
ID = 0
flip = True
for i in range(len(inp)):
    if flip:
        for j in range(inp[i]):
            disk.append(ID)
        ID+=1
    else:
        for j in range(inp[i]):
            disk.append('.')
    flip = not flip

print(disk)
empty=0
i=0
while i<len(disk):
    while disk[-1] == '.':
        disk.pop()
    if disk[i] == '.':
        disk[i] = disk.pop(-1)
        #print(disk)
    i+=1
s=0
for i in range(len(disk)):
    s+=i*disk[i]
print(s)
