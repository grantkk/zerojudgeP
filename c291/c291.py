n = int(input())
friend = [int(x) for x in input().split()]
mark = [0 for i in range(n)]
groups = []
for i in range(n):
    group = []
    j = i
    while mark[i] == 0:
        group.append(friend[j])
        j = friend[j]
        mark[j] = -1
    if len(group) > 0:
        groups.append(group)

print(len(groups))

# print(groups)
# print(friend)
# print(mark)
