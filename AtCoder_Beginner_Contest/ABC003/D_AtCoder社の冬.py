from math import comb

R, C = map(int, input().split())
X, Y = map(int, input().split())
D, L = map(int, input().split())

# RC領域内のXY領域の配置パターン数
pattern_XY = (R - X + 1) * (C - Y + 1)

# デスクとラックの合計数
sum_DL = D + L

# XY領域内のデスク+ラック領域の配置パターン数
# 包除原理を利用
# 全体から選ぶ場合
comb_XY = comb(X * Y, sum_DL)
# 上または下の1行が空になる場合
comb_XY -= 2 * comb((X - 1) * Y, sum_DL)
# 左または右の1列が空になる場合
comb_XY -= 2 * comb(X * (Y - 1), sum_DL)
# 上か下の1行と右か左の1列が空になる場合
comb_XY += 4 * comb((X - 1) * (Y - 1), sum_DL)
# 上下の2行が空になる場合
if X >= 2:
    comb_XY += comb((X - 2) * Y, sum_DL)
# 左右の2列が空になる場合
if Y >= 2:
    comb_XY += comb(X * (Y - 2), sum_DL)
# 上下2行と左か右の1列が空になる場合
if X >= 2:
    comb_XY -= 2 * comb((X - 2) * (Y - 1), sum_DL)
# 左右2列と上か下の1行が空になる場合
if Y >= 2:
    comb_XY -= 2 * comb((X - 1) * (Y - 2), sum_DL)
# 上下2行と左右2列が全て空になる場合
if X >= 2 and Y >= 2:
    comb_XY += comb((X - 2) * (Y - 2), sum_DL)

# デスク+ラック領域内の配置パターン数
comb_DL = comb(sum_DL, D)

# XY領域内のデスクとラックの配置パターン数
pattern_DL = comb_XY * comb_DL

print((pattern_XY * pattern_DL) % (10 ** 9 + 7))
