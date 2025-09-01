N = int(input())
S = input()

# "ABABAB..."の形にするために必要な操作回数
count_AB = 0
# "BABABA..."の形にするために必要な操作回数
count_BA = 0
# "A"が現れた回数
count_A = 0

for i in range(2 * N):
    if S[i] == "A":
        count_AB += abs(i - count_A * 2)
        count_BA += abs(i - (count_A * 2 + 1))
        count_A += 1

print(min(count_AB, count_BA))
