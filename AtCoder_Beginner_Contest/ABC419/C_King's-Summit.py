N = int(input())
R, C = [], []
for _ in range(N):
    r, c = map(int, input().split())
    R.append(r)
    C.append(c)

diff_R = max(R) - min(R)
diff_C = max(C) - min(C)
max_diff = max(diff_R, diff_C)

print((max_diff + 1) // 2)
