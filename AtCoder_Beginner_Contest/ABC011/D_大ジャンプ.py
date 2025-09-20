from math import comb

N, D = map(int, input().split())
X, Y = map(int, input().split())

if X % D == 0 and Y % D == 0:
    # Dで正規化して、Dを1とみなす
    X //= D
    Y //= D

    # (X+Y)とNの偶奇が一致しなければ到達不可
    if (X + Y) % 2 != N % 2:
        print(0)

    else:
        # u: 右または上に進んだジャンプ回数
        u = (X + Y + N) // 2
        # v: 右または下に進んだジャンプ回数
        v = (X - Y + N) // 2

        # ジャンプの回数は 0..N の範囲でなければ不可能
        if not (0 <= u <= N and 0 <= v <= N):
            print(0)
        else:
            print(comb(N, u) * comb(N, v) / (4 ** N))

else:
    print(0)
