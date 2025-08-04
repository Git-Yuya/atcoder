S = input()

# 荷物の個数
num = 0

for i in range(len(S)):
    if S[i] == "#":
        num += 1
        if num % 2 == 1:
            print(i + 1, end="")
            print(",", end="")
        else:
            print(i + 1)
