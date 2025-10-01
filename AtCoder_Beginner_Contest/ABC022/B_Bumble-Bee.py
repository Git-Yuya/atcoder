N = int(input())

visited_flowers = set()
count = 0

for _ in range(N):
    A = int(input())

    if A in visited_flowers:
        count += 1
    else:
        visited_flowers.add(A)

print(count)
