S = list(input())

# ボタンを押す回数
count = 1
# 何文字目か
index = 1

while index < len(S):
    if index + 1 < len(S) and S[index] == "0" and S[index + 1] == "0":
        index += 2
    else:
        index += 1

    count += 1

print(count)


# ========== 別解 ==========
S = input()

print(len(S) - S.count("00"))
