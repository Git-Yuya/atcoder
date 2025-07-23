N = int(input())
P = list(map(int, input().split()))

# 数列間の大小関係
plus_minus_list = [0] * (N - 1)

for i in range(N - 1):
    if P[i] < P[i + 1]:
        plus_minus_list[i] = 1
    else:
        plus_minus_list[i] = -1

# 数列間の大小と連続する個数
plus_minus_count_list = []
# 連続する個数
plus_minus_count = 1

for i in range(N - 2):
    if plus_minus_list[i] == plus_minus_list[i + 1]:
        plus_minus_count += 1
    else:
        plus_minus_count_list.append((plus_minus_list[i], plus_minus_count))
        plus_minus_count = 1
plus_minus_count_list.append((plus_minus_list[-1], plus_minus_count))

# チルダ型部分数列の個数
count = 0

for i in range(len(plus_minus_count_list) - 2):
    if plus_minus_count_list[i][0] == -1:
        continue

    count += plus_minus_count_list[i][1] * plus_minus_count_list[i + 2][1]

print(count)


# ========== 別解 ==========
import sys

N = int(sys.stdin.readline())
P = [int(x) for x in sys.stdin.readline().split(" ")]

# チルダ型部分数列の個数
count = 0
# 直前の増加部分の長さ
prev_increasing_length = 0
# 現在の増加部分の長さ
current_increasing_length = 0

for i in range(1, N):
    if P[i - 1] < P[i]:
        # 増加が続く場合、直前の増加部分の長さを加算
        count += prev_increasing_length
        current_increasing_length += 1

    if P[i - 1] > P[i]:
        if current_increasing_length > 0:
            # 増加から減少に転じたら、直前の増加部分の長さを保存
            prev_increasing_length = current_increasing_length
            current_increasing_length = 0

print(count)
