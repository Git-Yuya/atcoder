N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

# 最大の非負整数
max_x = 0

for x in range(1, N + 1):
    if A[x - 1] >= x:
        max_x = x

print(max_x)


# ========== 別解 ==========
N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)

ans = 0

for i in range(N):
    x = min(A[i], i + 1)
    ans = max(ans, x)

print(ans)
