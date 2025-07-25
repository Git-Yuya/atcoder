N, K = map(int, input().split())
A = list(map(int, input().split()))

num = 1

for a in A:
    num *= a

    if num >= 10 ** K:
        num = 1

print(num)
