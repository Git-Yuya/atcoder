N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

# xが存在するかどうか
is_exist = True
# xの最小値
min_x = A[0]

for i in range(N - 1):
    if A[i] > B[i]:
        is_exist = False
        break

    # 次のおもちゃが現在の箱より重い場合
    if A[i + 1] > B[i]:
        min_x = A[i + 1]

print(min_x if is_exist else -1)
