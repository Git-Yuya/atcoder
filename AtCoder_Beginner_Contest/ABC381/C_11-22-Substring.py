N = int(input())
S = input()

# 11/22文字列の最大の長さ
max_length = 0

for i, s in enumerate(S):
    if s == "/":
        # 両サイドに伸びる1と2の数
        length_12 = 0
        while True:
            if (i - 1 - length_12 >= 0) and (i + 1 + length_12 < N):
                if S[i - 1 - length_12] == "1" and S[i + 1 + length_12] == "2":
                    length_12 += 1
                else:
                    break
            else:
                break
        max_length = max(max_length, length_12 * 2 + 1)

print(max_length)


# ========== 別解 ==========
import re

N = int(input())
S = input()

# 11/22文字列の最大の長さ
max_length = 1

# 正規表現
for s in re.findall(r"1+/2+", S):
    p = s.split("/")
    length_12 = min(len(p[0]), len(p[1]))
    max_length = max(max_length, length_12 * 2 + 1)

print(max_length)
