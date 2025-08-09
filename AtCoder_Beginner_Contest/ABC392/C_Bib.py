from collections import defaultdict

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

# キー：ゼッケン、値：人
bibs = defaultdict(int)
for i, q in enumerate(Q):
    bibs[q] = i + 1

ans = []
for qi in range(1, N + 1):
    # ゼッケンqiを着けている人が見つめている人
    p = P[bibs[qi] - 1]
    # 見つめられている人が着けているゼッケン
    bib = Q[p - 1]
    ans.append(bib)

print(*ans)


# ========== 別解 ==========
import sys
input = sys.stdin.readline

N = int(input())
P = [int(x) - 1 for x in input().split()]
Q = [int(x) - 1 for x in input().split()]

res = [0] * N
for i, q in enumerate(Q):
    res[q] = Q[P[i]] + 1

print(" ".join(map(str, res)))
