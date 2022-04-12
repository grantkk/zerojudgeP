k = int(input())
str1 = input()

# print(ord("a"))
# print(ord("z"))
# print(ord("A"))
# print(ord("Z"))

# print(str1)
str2 = []
str3 = []
if (ord(str1[0]) >= ord("a")) and (ord(str1[0]) <= ord("z")):
    pre = 0
else:
    pre = 1
count = 0
for s in str1:
    if (ord(s) >= ord("a")) and (ord(s) <= ord("z")):
        cur = 0
        if pre != cur:
            str3.append(count)
            count = 0
        pre = cur
        count += 1
        str2.append(0)
    else:
        cur = 1
        if pre != cur:
            str3.append(count)
            count = 0
        pre = cur
        count += 1
        str2.append(1)
str3.append(count)
# print(k)
# print(str2)
# print(str3)
maxnum = 0
count = 0
for i in str3:
    if i < k:
        maxnum = max(maxnum, count)
        count = 0
    elif i > k:
        maxnum = max(maxnum, count + k)
        count = k
    else:
        count += k
maxnum = max(maxnum, count)

print(maxnum)
