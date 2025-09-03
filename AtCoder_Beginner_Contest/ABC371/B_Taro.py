N, M = map(int, input().split())

# 家に長男がいるかどうか
is_first_boy = [False] * N

for i in range(M):
    A, B = input().split()
    A = int(A) - 1

    if B == "M" and not is_first_boy[A]:
        is_first_boy[A] = True
        print("Yes")
    else:
        print("No")
