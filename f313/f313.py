def refreshmatrix():
    global rows, r, c, k, moverows
    for i in range(r):
        for j in range(c):
            rows[i][j] += moverows[i][j]
            moverows[i][j] = 0


def move1(i, j, count):
    global rows, r, c, k, moverows
    if i >= 0 and i < r and j >= 0 and j < c and rows[i][j] != -1:
        # rows[i][j] += count
        moverows[i][j] += count
        # print(f"---move {i}-{j}:{count}:{rows[i][j]}---")
        return count
    else:
        return 0


def migrate():
    global rows, r, c, k
    for i in range(r):
        for j in range(c):
            if rows[i][j] == -1:
                pass
                # print("No move")
            else:
                # print(f"move:{i}-{j}:{rows[i][j]}")
                rows[i][j] -= move1(i - 1, j, rows[i][j] // k)
                rows[i][j] -= move1(i + 1, j, rows[i][j] // k)
                rows[i][j] -= move1(i, j - 1, rows[i][j] // k)
                rows[i][j] -= move1(i, j + 1, rows[i][j] // k)
                # print(f"{rows[i][j]}")
    refreshmatrix()


r, c, k, m = map(int, input().split(" "))
row = []
rows = []
moverows = []
for i in range(r):
    row = list(map(int, input().split(" ")))
    rows.append(row)
    moverows.append([0 for x in range(c)])


# print(rows)
# print(moverows)
# print(r, c, k, m)


for i in range(m):
    migrate()
    # print(rows)
maximum = 0
minimum = 100
for i in range(r):
    for j in range(c):
        if maximum < rows[i][j]:
            maximum = rows[i][j]
        if (minimum > rows[i][j]) and rows[i][j] > 0:
            minimum = rows[i][j]

print(maximum, minimum)
