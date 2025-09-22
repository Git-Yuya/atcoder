N, H = map(int, input().split())
A, B, C, D, E = map(int, input().split())

min_cost = float("inf")

for x in range(N + 1):
    # H + Bx + Dy - (N - x - y)E > 0 より
    y = max(((N - x) * E - H - B * x) // (D + E) + 1, 0)

    if x + y > N:
        continue

    cost = A * x + C * y
    min_cost = min(min_cost, cost)

print(min_cost)
