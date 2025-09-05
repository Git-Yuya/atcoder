N = int(input())
A = list(map(int, input().split()))

# 等差数列の部分列の個数
count = N
# 連続数
l = 1
# 公差
d = 10 ** 9

for i in range(N - 1):
    if A[i + 1] - A[i] == d:
        l += 1
    else:
        d = A[i + 1] - A[i]
        l = 2

    count += l - 1

print(count)
