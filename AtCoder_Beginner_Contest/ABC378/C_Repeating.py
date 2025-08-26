from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
B = []

# 最後に現れたインデックス
latest_index = defaultdict(int)

for i in range(N):
    if A[i] in latest_index:
        B.append(latest_index[A[i]])
    else:
        B.append(-1)

    latest_index[A[i]] = i + 1

print(*B)
