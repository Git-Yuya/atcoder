R, C, K = map(int, input().split())
N = int(input())
r_list, c_list = [], []
for _ in range(N):
    r, c = map(int, input().split())
    r_list.append(r - 1)
    c_list.append(c - 1)

# それぞれの行と列の飴の個数
row_candy_count = [0] * R
col_candy_count = [0] * C
for i in range(N):
    r, c = r_list[i], c_list[i]
    row_candy_count[r] += 1
    col_candy_count[c] += 1

# 飴の個数に対する列の数
col_count = [0] * (N + 1)
for candy_count in col_candy_count:
    col_count[candy_count] += 1

# 飴の個数がK個になる組み合わせの数
count_A = 0
for candy_count in row_candy_count:
    if K - candy_count >= 0:
        count_A += col_count[K - candy_count]

# 飴があるマスのうち、飴の個数がK個になる組み合わせの数のうち
count_B = 0
# 飴があるマスのうち、飴の個数がK+1個になる組み合わせの数
count_C = 0
for i in range(N):
    r, c = r_list[i], c_list[i]
    total_candy = row_candy_count[r] + col_candy_count[c]
    if total_candy == K:
        count_B += 1
    elif total_candy == K + 1:
        count_C += 1

print(count_A - count_B + count_C)
