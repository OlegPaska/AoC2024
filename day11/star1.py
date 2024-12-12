stones = []
with open("in.txt") as f:
  for i in f.readline().split():
    stones.append(int(i))
print(stones)
def blink():
  i = 0
  while i < len(stones):
    stone = stones[i]
    if stone == 0:
      stones[i] = 1
    elif len(str(stone))%2 == 0:
      temp = stone
      stones[i] = int(str(temp)[:len(str(temp))//2])
      stones.insert(i+1, int(str(temp)[len(str(temp))//2:]))
      i+=1
    else:
      stones[i] = stone*2024
    i+=1

for i in range(25):
  blink()
  print(f"finished blink {i}")
print(len(stones))
