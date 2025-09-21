N = int(input())

diff = 2025 - N

for i in range(1, 10):
    for j in range(1, 10):
        if i * j == diff:
            print(f"{i} x {j}")
