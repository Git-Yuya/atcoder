n, X = map(int, input().split())
a = list(map(int, input().split()))

total_price = 0

for i in range(n):
    if X >> i & 1:
        total_price += a[i]

print(total_price)
