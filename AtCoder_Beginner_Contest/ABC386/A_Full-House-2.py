cards = list(map(int, input().split()))

# カードの種類ごとの枚数
kinds = [0] * 13
for card in cards:
    kinds[card - 1] += 1

if 3 in kinds and 1 in kinds:
    print("Yes")
elif kinds.count(2) == 2:
    print("Yes")
else:
    print("No")


# ========== 別解 ==========
cards = set(map(int, input().split()))

print("Yes" if len(cards) == 2 else "No")
