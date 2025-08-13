N = int(input())
A = list(map(int, input().split()))

# 等比数列かどうか
is_geometric = True

for i in range(2, N):
    if A[i - 1] ** 2 != A[i - 2] * A[i]:
        is_geometric = False
        break

print("Yes" if is_geometric else "No")
