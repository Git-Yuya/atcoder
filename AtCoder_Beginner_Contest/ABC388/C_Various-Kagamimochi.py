import bisect

N = int(input())
A = list(map(int, input().split()))

# 鏡餅の種類
kinds = 0

for a in A:
    index = bisect.bisect_left(A, a * 2)
    kinds += N - index

print(kinds)
