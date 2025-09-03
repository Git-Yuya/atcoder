N, Q = map(int, input().split())
S = list(input())

# 部分文字列"ABC"が含まれる個数
count_ABC = "".join(S).count("ABC")

for _ in range(Q):
    X, C = input().split()
    X = int(X) - 1

    # 置き換え前の影響
    for i in range(X - 2, X + 1):
        if 0 <= i <= N - 3:
            if S[i:i+3] == ["A", "B", "C"]:
                count_ABC -= 1

    # 置き換え
    S[X] = C

    # 置き換え後の影響
    for i in range(X - 2, X + 1):
        if 0 <= i <= N - 3:
            if S[i:i+3] == ["A", "B", "C"]:
                count_ABC += 1

    print(count_ABC)
