N, K = map(int, input().split())
S = input()

# 連続する丈夫な歯の数
teeth = []

count = 0
for s in S:
    if s == "O":
        count += 1
    else:
        if count > 0:
            teeth.append(count)
        count = 0
if count > 0:
    teeth.append(count)

print(sum(count // K for count in teeth if count >= K))


# ========== 別解 ==========
N, K = map(int, input().split())
S = input()

print(S.count("O" * K))
