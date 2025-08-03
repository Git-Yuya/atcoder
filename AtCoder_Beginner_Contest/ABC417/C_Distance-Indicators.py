from collections import Counter

N = int(input())
A = list(map(int, input().split()))

# j - A_j = i + A_i を満たす数
ans = 0

counter = Counter()
for i in range(N):
    key = i - A[i]
    ans += counter[key]
    counter[i + A[i]] += 1

print(ans)


# ========== 別解 ==========
N = int(input())
A = list(map(int, input().split()))

x = [0] * (4 * (10 ** 5))
ans = 0
for i in range(N):
    if i - A[i] >= 0:
        ans += x[i - A[i]]
    x[i + A[i]] += 1

print(ans)
