from itertools import product

N, K = map(int, input().split())
T = []
for i in range(N):
    T.append(list(map(int, input().split())))

for p in product(range(K), repeat=N):
    result = 0
    for i in range(N):
        result ^= T[i][p[i]]

    if result == 0:
        print("Found")
        break

else:
    print("Nothing")
