from collections import deque

N, K = map(int, input().split())

# A_NまでのK個の数列
A = deque([1] * K)
# K個の数列の和
sum_k = K
# 現在の値
if N < K:
    current = 1
else:
    current = K

for i in range(K + 1, N + 1):
    sum_k -= A.popleft()

    A.append(current)
    sum_k += current

    current = sum_k % (10 ** 9)

print(current)


# ========== 別解 ==========
N, K = map(int, input().split())

if N < K:
    print(1)
    exit()

A = [0] * (N + 1)
for i in range(K):
    A[i] = 1
A[K] = K

for i in range(K + 1, N + 1):
    A[i] = (2 * A[i - 1] - A[i - K - 1]) % (10 ** 9)

print(A[N])
