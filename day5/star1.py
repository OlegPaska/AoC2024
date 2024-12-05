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


for p in pages:
  valid = True
  p = p.split(',')
  for r in rules:
    nums = r.split('|')
    if nums[0] in p and nums[1] in p:
      if p.index(nums[0]) > p.index(nums[1]):
        valid = False
  if valid: total += int(p[(len(p))//2])
print(total)