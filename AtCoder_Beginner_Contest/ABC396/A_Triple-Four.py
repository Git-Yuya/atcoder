N = int(input())
A = list(map(int, input().split()))

# 連続箇所
count = 0

for i in range(1, N):
    if A[i] == A[i - 1]:
        count += 1
    else:
        count = 0

    if count == 2:
        print("Yes")
        break

else:
    print("No")


# ========== 別解 ==========
N = int(input())
A = list(map(int, input().split()))

for i in range(N - 2):
    if A[i] == A[i + 1] == A[i + 2]:
        print("Yes")
        exit()

print("No")
