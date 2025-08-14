N, D = map(int, input().split())
T, L = [], []
for _ in range(N):
    t, l = map(int, input().split())
    T.append(t)
    L.append(l)

for k in range(1, D + 1):
    W = [T[i] * (L[i] + k) for i in range(N)]
    print(max(W))
