N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 誰がどの美味しさの寿司を食べるか
sushi_eaters = [-1] * (2 * 10 ** 5 + 1)
# 現在の美食度の最小値
current_min_A = 2 * 10 ** 5 + 1

for i, a in enumerate(A, start=1):
    if a < current_min_A:
        sushi_eaters[a:current_min_A] = [i] * (current_min_A - a)
        current_min_A = a

for b in B:
    print(sushi_eaters[b])
