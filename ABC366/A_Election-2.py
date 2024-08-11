# 入力
N, T, A = map(int, input().split())

# 出力
if (T > (N / 2)) or (A > (N / 2)):
    print("Yes")
else:
    print("No")
