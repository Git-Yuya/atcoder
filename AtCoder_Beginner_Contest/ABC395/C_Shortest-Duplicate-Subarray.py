from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

# 各数字の位置
num_pos = defaultdict(list)
# 長さの最小値
min_length = float("inf")

for i, num in enumerate(A):
    if len(num_pos[num]) >= 1:
        min_length = min(min_length, i - num_pos[num][-1] + 1)
    num_pos[num].append(i)

if min_length == float("inf"):
    print(-1)
else:
    print(min_length)
