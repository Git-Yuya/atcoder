N = int(input())
A = list(map(int, input().split()))

# 操作回数
count = 0
# 操作を続けるかどうかのフラグ
is_continued = True

# 2で割る操作を繰り返す
while is_continued:
    for i in range(N):
        if A[i] % 2 == 0:
            A[i] = A[i] // 2
        else:
            is_continued = False
            break

    if is_continued:
        count += 1

print(count)


# ========== 別解 ==========
N = int(input())
A = list(map(int, input().split()))

# 操作回数
count = 0

# すべて偶数なら処理を繰り返す
while all(a % 2 == 0 for a in A):
    A = [a // 2 for a in A]
    count += 1

print(count)
