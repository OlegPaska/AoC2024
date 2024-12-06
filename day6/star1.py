grid = []
with open("in.txt", 'r') as f:
  grid = f.read().splitlines()

outOfBounds = False
visited = set()
#i cant count the amount of time ive misspelled guard
def move(dx, dy, guard):
  global outOfBounds
  global visited
  if guard[1] + dy >= 0 and guard[1] + dy < len(grid[1]) and guard[0] + dx >= 0 and guard[0] + dx < len(grid):
    if grid[guard[1] + dy][guard[0] + dx] != "#":
      guard[0] = guard[0] + dx
      guard[1] = guard[1] + dy
      visited.add((guard[0], guard[1]))
    else:
      guard[2] = (guard[2] + 1) % 4
  else:
    outOfBounds = True
  return 0


count = 0
#x,y,dir
guard = []
for y in range(len(grid)):
  if "^" in grid[y]:
    guard = [grid[y].index("^"), y, 0]
  if ">" in grid[y]:
    guard = [grid[y].index(">"), y, 1]
  if "v" in grid[y]:
    guard = [grid[y].index("v"), y, 2]
  if "<" in grid[y]:
    guard = [grid[y].index("<"), y, 3]
  

movement = [[0,-1], [1,0], [0,1], [-1,0]]
while not outOfBounds:
  count += move(movement[guard[2]][0], movement[guard[2]][1], guard)
print(len(visited))

