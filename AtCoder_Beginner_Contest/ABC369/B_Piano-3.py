N = int(input())

# 左手の位置
left_hand = -1
# 右手の位置
right_hand = -1
# 移動回数
move_count = 0

for _ in range(N):
    A, S = input().split()
    A = int(A)

    if S == "L":
        if left_hand != -1:
            move_count += abs(left_hand - A)
        left_hand = A

    else:
        if right_hand != -1:
            move_count += abs(right_hand - A)
        right_hand = A

print(move_count)
