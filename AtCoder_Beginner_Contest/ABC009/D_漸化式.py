def mul(A, B):
    n = len(A)
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][j] ^= A[i][k] & B[k][j]
    return res


def power(A, k):
    n = len(A)
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        res[i][i] = (1 << 32) - 1
    while k:
        if k & 1:
            res = mul(res, A)
        A = mul(A, A)
        k >>= 1
    return res


K, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

mat = [[0] * K for _ in range(K - 1)]
for j in range(K - 1):
    mat[j][j + 1] = (1 << 32) - 1
mat.append(C[::-1])
mat = power(mat, M - 1)

ans = 0
for j in range(K):
    ans ^= mat[0][j] & A[j]

print(ans)
