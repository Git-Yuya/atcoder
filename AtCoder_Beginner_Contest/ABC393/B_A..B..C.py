from collections import defaultdict

S = input()

# A, B, C の位置
position = defaultdict(list)
for i, c in enumerate(S):
    if c in "ABC":
        position[c].append(i)

# 2j = i + k を満たす箇所
count = 0
for a in position["A"]:
    for b in position["B"]:
        for c in position["C"]:
            if 2 * b == a + c and a < b < c:
                count += 1

print(count)


# ========== 別解 ==========
S = list(input())

ans = 0
for i in range(len(S)):
    if S[i] == "B":
        # "B"を中心に探索
        for j in range(min(i, len(S) - 1 - i) + 1):
            if S[i - j] == "A" and S[i + j] == "C":
                ans += 1

print(ans)
