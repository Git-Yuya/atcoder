N, K = map(int, input().split())
S = input()

# 連続する0と1のセグメント
segments = []
current_char = S[0]
current_length = 1

for i in range(1, N):
    if S[i] == current_char:
        current_length += 1
    else:
        segments.append((current_char, current_length))
        current_char = S[i]
        current_length = 1
segments.append((current_char, current_length))

# 入れ替え
if S[0] == "0":
    tmp = segments[2 * K - 1]
    segments[2 * K - 1] = segments[2 * K - 2]
    segments[2 * K - 2] = tmp
elif S[0] == "1":
    tmp = segments[2 * K - 2]
    segments[2 * K - 2] = segments[2 * K - 3]
    segments[2 * K - 3] = tmp

print("".join(char * length for char, length in segments))


# ========== 別解 ==========
N, K = map(int, input().split())
S = list(input().replace("10", "1,0").split(","))

# 0と1を逆順に入れ替え
S[K - 1] = S[K - 1][::-1]

print("".join(S))
