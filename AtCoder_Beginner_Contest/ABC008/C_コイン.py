N = int(input())
C = [int(input()) for _ in range(N)]

# 期待値
ev = 0

for i in range(N):
    # 約数の個数
    count = 0

    for j in range(N):
        if i == j:
            continue
        if C[i] % C[j] == 0:
            count += 1

    if count % 2 == 1:
        ev += 0.5
    else:
        ev += (count + 2) / (2 * count + 2)

print(ev)
