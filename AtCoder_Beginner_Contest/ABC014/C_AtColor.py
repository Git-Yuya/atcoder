n = int(input())

colors = [0] * (10 ** 6 + 2)

# いもす法
for _ in range(n):
    a, b = map(int, input().split())
    colors[a] += 1
    colors[b + 1] -= 1

for i in range(1, len(colors)):
    colors[i] += colors[i - 1]

print(max(colors))
