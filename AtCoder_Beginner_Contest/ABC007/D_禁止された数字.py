def f(n):
    # 桁DP
    # dp[tight][bad]:
    #   tight=0: ここまで上限nと一致, tight=1: 既にn未満が確定
    #   bad=0: まだ4か9を含んでいない, bad=1: 4か9を含んだことがある
    dp = [[0] * 2 for _ in range(2)]
    dp[0][0] = 1

    # 上位桁から1桁ずつ処理
    for x in list(str(n)):
        x = int(x)
        ndp = [[0] * 2 for _ in range(2)]
        for i in range(2):
            for j in range(2):
                for d in range(10):  # 桁の数字
                    if i == 0 and d > x:
                        continue
                    ni = i | (d < x)
                    nj = j | (d == 4 or d == 9)
                    ndp[ni][nj] += dp[i][j]
        dp = ndp

    return dp[0][1] + dp[1][1]


A, B = map(int, input().split())

print(f(B) - f(A - 1))
