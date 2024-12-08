grid = []
antinodes = set()
with open("in.txt") as f:
  grid = f.read().splitlines()
for i in range(len(grid)): grid[i] = list(grid[i])

def inBounds(guard, dx, dy):
    if guard[1] + dy >= 0 and guard[1] + dy < len(grid[1]) and guard[0] + dx >= 0 and guard[0] + dx < len(grid):
      return True
    else:
      return False

antenas = {}
for y in range(len(grid)):
  for x in range(len(grid)):
    g = grid[y][x]
    if g != '.':
      if g in antenas:
        antenas[g].append((x,y))
      else:
        antenas[g] = [(x,y)]
print(antenas)

for k in antenas:
  for a1 in antenas[k]:
    for a2 in antenas[k]:
      if a1 != a2:
        difference = (a1[0]-a2[0], a1[1]-a2[1])
        if inBounds(a1, difference[0], difference[1]):
          antinodes.add((a1[0]+difference[0], a1[1]+difference[1]))
        if inBounds(a2, difference[0]*-1, difference[1]*-1):
          antinodes.add((a2[0]+difference[0]*-1, a2[1]+difference[1]*-1))

for i in antinodes:
  grid[i[1]][i[0]] = '#'
print(grid)

print(antinodes)
print(len(antinodes))
print()