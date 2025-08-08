N = int(input())
S = [input() for _ in range(N)]

# 長さで昇順
S.sort(key=len)

print("".join(S))
