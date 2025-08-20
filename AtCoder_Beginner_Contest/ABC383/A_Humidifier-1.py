N = int(input())

water_amount = 0
prev_time = 0

for _ in range(N):
    T, V = map(int, input().split())
    water_amount = max(0, water_amount - (T - prev_time))
    water_amount += V
    prev_time = T

print(water_amount)
