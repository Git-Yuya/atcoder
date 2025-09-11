N, K = map(int, input().split())
R = list(map(int, input().split()))

R.sort()
C = 0.0

for i in range(K):
    rate = R[N - K + i]
    C = (C + rate) / 2

print(C)
