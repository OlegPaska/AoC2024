grid  = []
res = 0
visited = set()

with open("in.txt") as f:
  for i in f.read().splitlines():
    grid.append(list(i))

res = [0]
def dfs(x,y):
  directions = ((1,0), (0,1), (-1,0), (0,-1))
  visited.add((x,y))
  if grid[y][x] == '9':
    res[0] += 1
    return
  
  for d in directions:
    ny = y + d[1]
    nx = x + d[0]
    if ny in range(len(grid)) and nx in range(len(grid[ny])) and (nx,ny) not in visited and int(grid[ny][nx]) == int(grid[y][x])+1:
      dfs(nx,ny)

for y in range(len(grid)):
  for x in range(len(grid[0])):
    if grid[y][x] == '0':
      visited.clear()
      dfs(x,y)



print(sum(res))
print()