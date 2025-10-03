N, T = map(int, input().split())
A = [int(input()) for _ in range(N)]

total_time = T

for i in range(1, N):
    total_time += min(T, A[i] - A[i - 1])

print(total_time)
