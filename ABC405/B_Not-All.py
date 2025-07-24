N, M = map(int, input().split())
A = list(map(int, input().split()))

# 1以上M以下の整数が含まれているかどうか
is_exist_list = [False] * M

for i in range(N):
    if 1 <= A[i] <= M:
        is_exist_list[A[i] - 1] = True

        if all(is_exist_list):
            break

if all(is_exist_list):
    print(len(A) - i)
else:
    print(0)


# ========== 別解 ==========
N, M = map(int, input().split())
A = list(map(int, input().split()))

count = 0

while set(A) == set(range(1, M + 1)):
    A.pop()
    count += 1

print(count)
