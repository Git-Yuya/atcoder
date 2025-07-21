N = int(input())
A = list(map(int, input().split()))

C = set(A)
C = sorted(C)

print(len(C))
print(*C)
