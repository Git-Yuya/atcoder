N = int(input())
H = list(map(int, input().split()))

max_length = 1

for n in range(1, N):
    for i in range(n):
        current_value = -1
        current_length = 0

        # 先頭iからn個ずつのグループ分け
        for j in range(i, N, n):
            if H[j] != current_value:
                current_value = H[j]
                current_length = 1
            else:
                current_length += 1
            max_length = max(max_length, current_length)

print(max_length)
