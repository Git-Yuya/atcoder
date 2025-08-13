A = list(map(int, input().split()))

# [1,2,3,4,5]と同じかどうか
is_same = [True] * 5
for i in range(len(A)):
    if A[i] != i + 1:
        is_same[i] = False

for i in range(len(is_same) - 1):
    if is_same.count(False) == 2 and is_same[i] == False and is_same[i + 1] == False:
        print("Yes")
        break
else:
    print("No")


# ========== 別解 ==========
A = list(map(int, input().split()))

count = 1
for i in range(len(A) - 1):
    if A[i + 1] < A[i]:
        A[i], A[i + 1] = A[i + 1], A[i]
        count -= 1

print("Yes" if count == 0 else "No")
