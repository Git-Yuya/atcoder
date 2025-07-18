N = int(input())
D = list(map(int, input().split()))

for i in range(N - 1):
    distance = D[i]
    print(distance, end=" ")

    for j in range(i + 1, N - 1):
        distance += D[j]
        print(distance, end=" ")

    print()
