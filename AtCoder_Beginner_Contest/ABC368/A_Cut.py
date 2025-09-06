N, K = map(int, input().split())
A = list(map(int, input().split()))

for i in range(K):
    A.insert(0, A.pop())

print(*A)
