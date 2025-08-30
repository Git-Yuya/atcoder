import math

N = int(input())

total_cost = 0
current_x, current_y = 0, 0

for _ in range(N):
    X, Y = map(int, input().split())

    total_cost += math.sqrt((X - current_x) ** 2 + (Y - current_y) ** 2)
    current_x, current_y = X, Y
total_cost += math.sqrt(current_x ** 2 + current_y ** 2)

print(total_cost)
