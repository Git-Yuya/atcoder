import math

n = int(input())
k = int(input())

MOD = 10 ** 9 + 7

print(math.comb(n + k - 1, k) % MOD)


# ========== 別解 ==========
def fact(num):
    """ 階乗を計算 """
    prod = 1
    for i in range(1, num + 1):
        prod *= i
        prod %= MOD
    return prod


MOD = 10 ** 9 + 7

n = int(input())
k = int(input())

# フェルマーの小定理を利用
print(fact(n + k - 1) * pow(fact(k), MOD - 2, MOD) * pow(fact(n - 1), MOD - 2, MOD) % MOD)
