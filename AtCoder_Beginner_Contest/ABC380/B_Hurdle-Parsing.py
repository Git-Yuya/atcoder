S = input()
A = []

# "-"の連続数
count = 0

for s in S:
    if s == "-":
        count += 1
    elif s == "|":
        if count > 0:
            A.append(count)
        count = 0

print(*A)


# ========== 別解 ==========
S = input().split("|")

print(*[len(i) for i in S[1:-1]])
