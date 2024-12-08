from pqdm.processes import pqdm
import multiprocessing
import time
startTime = time.time()

targets = []
nums = []
ans = 0
with open("in.txt") as f:
  lines = f.read().splitlines()

for l in lines:
  targets.append(l.split(":")[0])
  nums.append(l.split(":")[1].strip().split(" "))

def ternary (n):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, 3)
        nums.append(str(r))
    return ''.join(reversed(nums))

def getRes(nums, ops):
  res = int(nums[0])
  for i in range(1, len(nums)):
    if ops[i-1] == "+":
      res += int(nums[i])
    if ops[i-1] == "*":
      res *= int(nums[i])
    #i spent an hour doing the concat before evaling the equation when i just had to add this
    if ops[i-1] == "|":
      res = int(str(res) + nums[i])
  return res
  

def process_line(ni):
  n = nums[ni]
  ans=0
  for i in range(pow(3,len(n)-1)):
    operators = ternary(i).zfill(len(n)-1)
    #print(operators)
    operators = operators.replace("0", "+")
    operators = operators.replace("1", "*")
    operators = operators.replace("2", "|")

    #cn, cops = doConcat(n,operators)
    s = ""
    for i in range(len(n)-1):
      s += n[i] + operators[i]
    s+= n[-1]

    if str(getRes(n, operators)) == targets[ni]:
      ans += getRes(n, operators)
      #print(f"{s} = {getRes(n, operators)}")
      break
  return ans
    
    

if __name__ == '__main__':
  print(ans)
  nis = [ni for ni in range(len(nums))]
  a = 0
  # for ni in nis:
  #   a += process_line(ni)
  # print(a)
  #res = pqdm(nis,process_line, n_jobs=20)
  p = multiprocessing.Pool(20)
  res = p.map(process_line, nis)
  a = sum(res)
  print(a)
  print("--- %s seconds ---" % (time.time() - startTime))
  #7 seconds pqdm
  #6 secs pool


