import multiprocessing
from functools import partial
import time

grid = []
with open("in.txt", 'r') as f:
  grid = f.read().splitlines()

for y in range(len(grid)):
  if "^" in grid[y]:
    startPos = [grid[y].index("^"), y, 0]
  if ">" in grid[y]:
    startPos = [grid[y].index(">"), y, 1]
  if "v" in grid[y]:
    startPos = [grid[y].index("v"), y, 2]
  if "<" in grid[y]:
    startPos = [grid[y].index("<"), y, 3]

outOfBounds = False
obstacles = []
count = 0
def move(grid, dx, dy, guard):
  global outOfBounds
  global obstacles
  global startPos
  #global guard
  if guard[1] + dy >= 0 and guard[1] + dy < len(grid[1]) and guard[0] + dx >= 0 and guard[0] + dx < len(grid):
    if grid[guard[1] + dy][guard[0] + dx] != "#":
      guard[0] = guard[0] + dx
      guard[1] = guard[1] + dy
    else:
      if guard in obstacles:
        return True
      else:
        obstacles.append(guard[:])
      guard[2] = (guard[2] + 1) % 4

  else:
    outOfBounds = True
  return False


def process_row(y):
  global outOfBounds
  global obstacles
  ycount = 0
  global startPos
  movement = [[0,-1], [1,0], [0,1], [-1,0]]
  for x in range(len(grid[0])):
    print("testing {},{}".format(x,y) )
    guard = startPos[:]
    outOfBounds = False
    obstacles.clear()
    newGrid = []
    for i in grid:
      newGrid.append(list(i))
    newGrid[y][x] = "#"
    while not outOfBounds:
      if move(newGrid, movement[guard[2]][0], movement[guard[2]][1], guard):
        ycount+=1
        print(x,y)
        break
  return ycount

def main():
  global count
  global startPos
  #x,y,dir


  pool = multiprocessing.Pool(multiprocessing.cpu_count())
  work = []
  for i in range(len(grid)):
    work.append(i)

  res = pool.map(process_row, work)
  print(sum(res))

if __name__ == "__main__":
  startTime = time.time()
  main()
  print("--- %s seconds ---" % (time.time() - startTime))
  #4.5 seconds
