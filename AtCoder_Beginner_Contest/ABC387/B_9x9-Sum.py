from collections import defaultdict

X = int(input())

# 9x9表の各要素の積をカウント
num_count = defaultdict(int)
for i in range(1, 10):
    for j in range(1, 10):
        num_count[i * j] += 1

print(2025 - (X * num_count[X] if X in num_count else 0))


# ========== 別解 ==========
X = int(input())

ans = 0
for i in range(1, 10):
    for j in range(1, 10):
        if i * j == X:
            continue
        ans += i * j

print(ans)
