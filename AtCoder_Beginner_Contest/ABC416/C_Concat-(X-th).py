N, K, X = map(int, input().split())
S_list = [input() for _ in range(N)]

# 連結文字列
words = [""]

for i in range(K):
    new_words = []
    for word in words:
        for S in S_list:
            new_words.append(word + S)
    words = new_words

words.sort()
print(words[X - 1])


# ========== 別解 ==========
import itertools

N, K, X = map(int, input().split())
S = [input() for _ in range(N)]

ans = []
for v in itertools.product(S, repeat=K):
    ans.append("".join(v))

ans.sort()
print(ans[X - 1])


# ========== 別解 ==========
N, K, X = map(int, input().split())
S = [input() for _ in range(N)]

ans = []
def dfs(crr, count):
    if count == K:
        ans.append(crr)
        return
    else:
        for j in S:
            dfs(crr + j, count + 1)

dfs("", 0)
sorted_list = sorted(ans)
print(sorted_list[X - 1])
