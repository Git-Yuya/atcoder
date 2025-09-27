R, C, K = map(int, input().split())
grid = [input() for _ in range(R)]

a = [[False] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if grid[i][j] == "o":
            a[i][j] = True

for _ in range(K - 1):
    b = [a[i][:] for i in range(R)]
    for i in range(R):
        for j in range(C):
            if a[i][j] == False or i == 0 or i == R - 1 or j == 0 or j == C - 1:
                a[i][j] = False
            else:
                a[i][j] = b[i - 1][j] & b[i + 1][j] & b[i][j - 1] & b[i][j + 1]

count = 0
for i in range(R):
    for j in range(C):
        if a[i][j]:
            count += 1

print(count)
