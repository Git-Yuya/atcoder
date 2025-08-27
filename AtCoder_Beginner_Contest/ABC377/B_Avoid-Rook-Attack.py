S = []
for _ in range(8):
    S.append(input())

# 置けない行
invalid_rows = set()
# 置けない列
invalid_cols = set()

for i in range(8):
    for j in range(8):
        if S[i][j] == "#":
            invalid_rows.add(i)
            invalid_cols.add(j)

# 置けるマスの数
count = 0
for i in range(8):
    for j in range(8):
        if i not in invalid_rows and j not in invalid_cols:
            count += 1

print(count)


# ========== 別解 ==========
S = [input() for _ in range(8)]

# "."のみの行の数
r = sum(row == "." * 8 for row in S)
# "."のみの列の数
c = sum(all(row[i] == "." for row in S) for i in range(8))

print(r * c)
