X, Y = map(int, input().split())

count = 0
for i in range(1, 7):
    for j in range(1, 7):
        # 2つの出目の合計がX未満 かつ 2つの出目の差の絶対値がY未満
        if (i + j < X) and (abs(i - j) < Y):
            count += 1

# 余事象
print(1 - count / 36)


# ========== 別解 ==========
X, Y = map(int, input().split())

count = 0
for i in range(1, 7):
    for j in range(1, 7):
        if (i + j >= X) or (abs(i - j) >= Y):
            count += 1

print(count / 36)
