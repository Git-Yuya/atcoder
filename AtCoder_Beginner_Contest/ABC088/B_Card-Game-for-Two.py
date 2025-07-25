N = int(input())
a = list(map(int, input().split()))

# 降順にソート
a.sort(reverse=True)

# 得点
Alice_score = 0
Bob_score = 0

# それぞれの得点を計算
for i in range(N):
    if i % 2 == 0:
        Alice_score += a[i]
    else:
        Bob_score += a[i]

print(Alice_score - Bob_score)


# ========== 別解 ==========
N = int(input())
a = list(map(int, input().split()))

# 降順にソート
a.sort(reverse=True)

# それぞれの得点を計算
Alice_score = sum(a[i] for i in range(0, N, 2))
Bob_score = sum(a[i] for i in range(1, N, 2))

print(Alice_score - Bob_score)
