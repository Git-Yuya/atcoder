A = list(map(int, input().split()))

if A[0] == A[1] * A[2]:
    print("Yes")
elif A[1] == A[0] * A[2]:
    print("Yes")
elif A[2] == A[0] * A[1]:
    print("Yes")
else:
    print("No")


# ========== 別解 ==========
A = list(map(int, input().split()))
A.sort()

if A[0] * A[1] == A[2]:
    print("Yes")
else:
    print("No")
