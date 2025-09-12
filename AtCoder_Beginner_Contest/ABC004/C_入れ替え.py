N = int(input())

cards = [num for num in range(1, 7)]

for i in range(N % 30):
    cards[i % 5], cards[i % 5 + 1] = cards[i % 5 + 1], cards[i % 5]

print("".join(map(str, cards)))
