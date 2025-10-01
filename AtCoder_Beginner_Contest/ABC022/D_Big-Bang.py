N = int(input())
A = [tuple(map(int, input().split())) for _ in range(N)]
B = [tuple(map(int, input().split())) for _ in range(N)]

# Aの重心
cog_A = (sum(a[0] for a in A) / N, sum(a[1] for a in A) / N)
# Bの重心
cog_B = (sum(b[0] for b in B) / N, sum(b[1] for b in B) / N)

# Aの重心から一番遠い点までの距離
max_dist_A = -1
for a in A:
    dist = ((a[0] - cog_A[0]) ** 2 + (a[1] - cog_A[1]) ** 2) ** 0.5
    max_dist_A = max(max_dist_A, dist)

# Bの重心から一番遠い点までの距離
max_dist_B = -1
for b in B:
    dist = ((b[0] - cog_B[0]) ** 2 + (b[1] - cog_B[1]) ** 2) ** 0.5
    max_dist_B = max(max_dist_B, dist)

print(max_dist_B / max_dist_A)
