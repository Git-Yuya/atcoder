N, L, R = map(int, input().split())

# 最初から最後まで見ることができるリスナーの人数
count = 0

for _ in range(N):
    X, Y = map(int, input().split())
    if X <= L and Y >= R:
        count += 1

print(count)
