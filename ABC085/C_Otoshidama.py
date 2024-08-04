# 入力
N, Y = map(int, input().split())

# x, y, z の組み合わせ
bill = [-1, -1, -1]

# 繰り返し処理
for x in range(N + 1):
    for y in range(N - x + 1):
        z = N - x - y
        total = 10000 * x + 5000 * y + 1000 * z
        if total == Y:
            bill = [x, y, z]

# 出力
print(f"{bill[0]} {bill[1]} {bill[2]}")




##### 別解 #####
# def find_combination(N: int, Y: int) -> None:
#     """
#     合計金額Yとなるようなお札の組み合わせを出力する関数
    
#     Args:
#         N (int): お札の総枚数
#         Y (int): 合計金額
#     """
#     for x in range(N + 1):
#         for y in range(N - x + 1):
#             z = N - x - y
#             total = 10000 * x + 5000 * y + 1000 * z
#             if total == Y:
#                 print(x, y, z)
#                 return
#     print(-1, -1, -1)


# # 入力
# N, Y = map(int, input().split())

# # 出力
# find_combination(N, Y)
