S = input()

# "t"のindex
t_index = []
for i in range(len(S)):
    if S[i] == "t":
        t_index.append(i)

# 充填率の最大値
max_fill_rate = 0
for i in range(len(t_index) - 1):
    for j in range(i + 1, len(t_index)):
        if t_index[j] - t_index[i] > 1:
            fill_rate = (len(t_index[i:j+1]) - 2) / (t_index[j] - t_index[i] + 1 - 2)
            max_fill_rate = max(max_fill_rate, fill_rate)

print(max_fill_rate)
