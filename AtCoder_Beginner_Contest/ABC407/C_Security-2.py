S = list(input())

# ボタンAを押す
count = len(S)

for i in range(len(S) - 1):
    # 次の数字との差
    if int(S[i]) >= int(S[i + 1]):
        diff = int(S[i]) - int(S[i + 1])
    else:
        diff = int(S[i]) - int(S[i + 1]) + 10

    # 差の分だけボタンBを押す
    count += diff

# 目的の数字にするためにボタンBを押す
count += int(S[-1])

print(count)


# ========== 別解 ==========
S = input() + "0"

count = len(S) - 1

for i in range(len(S) - 1):
    count += (ord(S[i]) - ord(S[i + 1])) % 10

print(count)
