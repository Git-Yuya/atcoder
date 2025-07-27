N = int(input())
A = list(map(int, input().split()))

print(sum(A[i] for i in range(0, N, 2)))
