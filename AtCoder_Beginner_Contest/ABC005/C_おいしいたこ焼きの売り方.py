T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

# 食べられたたこ焼き
is_eaten = [False] * N

for b in B:
    for i in range(N):
        if not is_eaten[i] and A[i] <= b <= A[i] + T:
            is_eaten[i] = True
            break

print("yes" if is_eaten.count(True) == M else "no")
