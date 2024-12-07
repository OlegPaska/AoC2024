targets = []
nums = []
ans = 0
with open("in.txt") as f:
  lines = f.read().splitlines()

for l in lines:
  targets.append(l.split(":")[0])
  nums.append(l.split(":")[1].strip().split(" "))

def getRes(nums, ops):
  res = int(nums[0])
  for i in range(1, len(nums)):
    if ops[i-1] == "+":
      res += int(nums[i])
    if ops[i-1] == "*":
      res *= int(nums[i])
  return res
  

for ni in range(len(nums)):
  n = nums[ni]
  for i in range(pow(2,len(n)-1)):
    operators = bin(i)[2:].zfill(len(n)-1)
    operators = operators.replace("0", "+")
    operators = operators.replace("1", "*")
    s = ""
    res = n[0]
    for i in range(len(n)-1):
      s += n[i] + operators[i]
    s+= n[-1]

    if str(getRes(n, operators)) == targets[ni]:
      ans += getRes(n, operators)
      print(f"{s} = {getRes(n, operators)}")
      break
    
    


print(ans)
      



