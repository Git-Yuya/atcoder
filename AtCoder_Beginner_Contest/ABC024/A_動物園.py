A, B, C, K = map(int, input().split())
S, T = map(int, input().split())

total_fee = A * S + B * T
if S + T >= K:
    total_fee -= C * (S + T)

print(total_fee)
