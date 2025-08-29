N, C = map(int, input().split())
T = list(map(int, input().split()))

count = 1
previous_time = T[0]

for i in range(1, len(T)):
    if T[i] - previous_time >= C:
        previous_time = T[i]
        count += 1

print(count)
