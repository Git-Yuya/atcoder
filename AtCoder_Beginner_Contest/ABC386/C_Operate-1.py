K = int(input())
S = input()
T = input()

if S == T:
    print("Yes")

# 変更判定
elif len(S) == len(T):
    diff_count = sum(1 for s, t in zip(S, T) if s != t)
    if diff_count <= K:
        print("Yes")
    else:
        print("No")

# Sに1文字挿入 = Tの1文字削除
elif len(S) + 1 == len(T):
    # 先頭何文字一致しているか
    head_count = 0
    while head_count < len(S):
        if S[head_count] == T[head_count]:
            head_count += 1
        else:
            break

    # 末尾何文字一致しているか
    tail_count = 0
    while tail_count < len(S):
        if S[-(tail_count + 1)] == T[-(tail_count + 1)]:
            tail_count += 1
        else:
            break

    # 一致している文字数が|S|以上ならYes
    if head_count + tail_count >= len(S):
        print("Yes")
    else:
        print("No")

# Tに1文字挿入 = Sの1文字削除
elif len(S) == len(T) + 1:
    # 先頭何文字一致しているか
    head_count = 0
    while head_count < len(T):
        if S[head_count] == T[head_count]:
            head_count += 1
        else:
            break

    # 末尾何文字一致しているか
    tail_count = 0
    while tail_count < len(T):
        if S[-(tail_count + 1)] == T[-(tail_count + 1)]:
            tail_count += 1
        else:
            break

    # 一致している文字数が|T|以上ならYes
    if head_count + tail_count >= len(T):
        print("Yes")
    else:
        print("No")

else:
    print("No")


# ========== 別解 ==========
K = int(input())
S = input()
T = input()

len_S = len(S)
len_T = len(T)

# 先頭から何文字目が不一致か
idx = 0
for i in range(min(len_S, len_T)):
    if S[i] != T[i]:
        idx = i
        break
else:
    idx = i + 1

if len_S == len_T:
    print("Yes" if S[idx+1:] == T[idx+1:] else "No")
elif len_S + 1 == len_T:
    print("Yes" if S[idx:] == T[idx+1:] else "No")
elif len_S == len_T + 1:
    print("Yes" if S[idx+1:] == T[idx:] else "No")
else:
    print("No")
