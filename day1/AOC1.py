f = open("in.txt", 'r')
l1 = []
l2 = []
for line in f:
  n, m = map(int, line.split('   '))
  l1.append(int(line.split()[0]))
  l2.append(int(line.split()[1]))
#q1
# l1.sort()
# l2.sort()
# diff = 0
# for i in range(len(l1)):
#   diff += abs(l1[i]-l2[i])
# print(diff)

#q2 o(n^2)
similarity = 0
for i in l1:
  occurances = 0
  for j in l2:
    if j == i:
      occurances +=1
  similarity += occurances * i
print(similarity)