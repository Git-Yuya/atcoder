Q = int(input())

# カードの山
cards = [0] * 100

for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        x = query[1]
        cards.append(x)

    elif query[0] == 2:
        print(cards.pop())
