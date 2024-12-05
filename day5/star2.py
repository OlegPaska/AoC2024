rules = []
pages = []
total = 0
with open("in.txt", 'r') as f:
  lines = f.read().splitlines()
  for l in lines:
    if pages or l == "":
      pages.append(l)
    else:
      rules.append(l)
  pages.pop(0)

def checkValid(p):
  valid = True
  for r in rules:
    nums = r.split('|')
    if nums[0] in p and nums[1] in p:
      if p.index(nums[0]) > p.index(nums[1]):
        valid = False
  return valid

def makeValid(p):
  while not checkValid(p):
    for r in rules:
      r = r.split('|')
      if r[0] in p and r[1] in p:
        if p.index(r[0]) > p.index(r[1]):
          temp = p[p.index(r[0])]
          p[p.index(r[0])] = p[p.index(r[1])]
          p[p.index(r[1])] = temp
  return int(p[(len(p))//2])


for p in pages:
  p = p.split(',')
  if not checkValid(p):
    total += makeValid(p)

print(total)
  