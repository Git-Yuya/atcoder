A = int(input())
B = int(input())
C = int(input())

MOD = 10 ** 9 + 7

# フェルマーの小定理を利用して逆元を計算
x = A * pow(B, MOD - 2, MOD)
y = A * pow(C, MOD - 2, MOD)
z = pow(x + y - 1, MOD - 2, MOD)

print((y * z - 1) % MOD, (x * z - 1) % MOD)
