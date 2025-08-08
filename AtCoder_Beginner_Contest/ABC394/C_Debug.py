S = input()

# "W"の連続数
count_W = 0

for i in range(len(S)):
    if S[i] == "W":
        count_W += 1
    elif S[i] == "A":
        if count_W > 0:
            S = S[:i-count_W] + "A" + "C" * count_W + S[i+1:]
            count_W = 0
    else:
        count_W = 0

print(S)


# ========== 別解 ==========
S = input()

result = ""
count_W = 0

for ch in S:
    if ch == "W":
        count_W += 1

    elif ch == "A":
        if count_W > 0:
            result += "A" + ("C" * count_W)
            count_W = 0
        else:
            result += "A"

    else:
        if count_W > 0:
            result += "W" * count_W
            count_W = 0
        result += ch

if count_W > 0:
    result += "W" * count_W

print(result)
