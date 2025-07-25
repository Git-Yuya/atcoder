N, Y = map(int, input().split())

# x, y, z の組み合わせ
bill = [-1, -1, -1]

# N枚のお札を使って合計金額Yを作る組み合わせを探索
for x in range(N + 1):
    for y in range(N - x + 1):
        z = N - x - y
        total = 10000 * x + 5000 * y + 1000 * z
        if total == Y:
            bill = [x, y, z]
            break

print(f"{bill[0]} {bill[1]} {bill[2]}")


# ========== 別解 ==========
def find_combination(N: int, Y: int) -> None:
    """
    合計金額Yとなるようなお札の組み合わせを出力する関数

    Args:
        N (int): お札の総枚数
        Y (int): 合計金額
    """
    for x in range(N + 1):
        for y in range(N - x + 1):
            z = N - x - y
            total = 10000 * x + 5000 * y + 1000 * z
            if total == Y:
                print(x, y, z)
                return

    print(-1, -1, -1)


N, Y = map(int, input().split())

find_combination(N, Y)
