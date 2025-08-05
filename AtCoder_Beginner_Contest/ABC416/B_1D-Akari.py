S = input()

# 求める文字列
T = ""
# "o"にできるかどうか
is_possible = True

for i in range(len(S)):
    if S[i] == ".":
        if is_possible:
            T += "o"
        else:
            T += "."
        is_possible = False

    elif S[i] == "#":
        T += "#"
        is_possible = True

print(T)


# ========== 別解 ==========
S = list(input())

for i in range(1, len(S)):
    if S[i - 1] == "." and S[i] == "#":
        S[i - 1] = "o"

if S[-1] == ".":
    S[-1] = "o"

print("".join(S))
