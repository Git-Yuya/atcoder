from collections import Counter


def min_cost(n: int, s_counter: Counter, t_counter: Counter) -> int:
    res = 0
    for c in map(chr, range(ord("a"), ord("z") + 1)):
        res += min(s_counter.get(c, 0), t_counter.get(c, 0))
    return n - res


N, K = map(int, input().split())
S = input()

T = []

s_counter = Counter(S)
t_counter = Counter(S)

# 不一致数
diff = 0

for i in range(N):
    s_counter[S[i]] -= 1

    for c in sorted(t_counter):
        if t_counter[c] == 0:
            continue
        t_counter[c] -= 1
        diff += c != S[i]

        if min_cost(N - i - 1, s_counter, t_counter) <= K - diff:
            T.append(c)
            break
        t_counter[c] += 1
        diff -= c != S[i]

print("".join(T))
