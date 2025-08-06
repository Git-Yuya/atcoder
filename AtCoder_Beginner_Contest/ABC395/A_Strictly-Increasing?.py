N = int(input())
A = list(map(int, input().split()))

for i in range(1, N):
    if A[i - 1] >= A[i]:
        print("No")
        break
else:
    print("Yes")
