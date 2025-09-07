N, K = map(int, input().split())
R = list(map(int, input().split()))


def solve(a):
    if len(a) == N:
        if sum(a) % K == 0:
            print(*a)
        return

    for x in range(1, R[len(a)] + 1):
        solve(a + [x])


solve([])
