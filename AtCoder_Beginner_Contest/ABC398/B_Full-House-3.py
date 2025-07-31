A = list(map(int, input().split()))

# カードの枚数
card_count = [0] * 13
for card in A:
    card_count[card - 1] += 1

# 降順にソート
card_count.sort(reverse=True)

if card_count[0] >= 3 and card_count[1] >= 2:
    print("Yes")
else:
    print("No")
