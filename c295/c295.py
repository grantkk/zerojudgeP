import pprint

n, m = map(int, input().split())

lsts = []
maxnums = []
for i in range(n):
    lst = []
    lst = [int(x) for x in input().split()]
    lsts.append(lst)
    maxnums.append(max(lst))

# pprint.pprint(lsts)
# pprint.pprint(maxnums)
sum1 = sum(maxnums)
print(sum1)
s = ""
for maxnum in maxnums:
    if sum1 % maxnum == 0:
        s = s + str(maxnum) + " "
s = s.strip()
if s == "":
    print("-1")
else:
    print(s)
