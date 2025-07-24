N = int(input())
A = list(map(int, input().split()))

sum_A = sum(A)
sum_AA = 0

for i in range(N):
    sum_A -= A[i]
    sum_AA += A[i] * sum_A

print(sum_AA)


# ========== 別解 ==========
N = int(input())
A = list(map(int, input().split()))

sum_A = sum(A)
sum_A_squared = sum(a ** 2 for a in A)

# Aの全要素の合計の2乗から各要素の2乗の合計を引き、重複を避けるため2で割る
ans = (sum_A ** 2 - sum_A_squared) // 2
print(ans)
