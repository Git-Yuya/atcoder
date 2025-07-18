def count_black(count: int, squares: list[int], a: int, sign: int) -> int:
    """
    追加する両サイドの状態を考慮して、黒いマスの数をカウント

    Args:
        count (int): 現在の黒いマスの数
        squares (list[int]): 各マスの状態を表すリスト
        a (int): 現在のクエリのインデックス
        sign (int): 1ならばカウントを増加、-1ならばカウントを減少

    Returns:
        count (int): 黒いマスの数
    """
    if squares[a] == 0 and squares[a + 1] == 1:
        count += sign

    return count


N, Q = map(int, input().split())
A = list(map(int, input().split()))

# 両端にマスを追加
squares = [0] * (N + 2)
count = 0

for q in range(Q):
    # 反転前
    count = count_black(count, squares, A[q] - 1, -1)
    count = count_black(count, squares, A[q], -1)

    squares[A[q]] ^= 1

    # 反転後
    count = count_black(count, squares, A[q] - 1, 1)
    count = count_black(count, squares, A[q], 1)

    print(count)


# ========== 別解 ==========
N, Q = map(int, input().split())

# 各マスの状態を管理するリスト
d = [0] * (N + 1)
# 黒マスの数
now = 0

for a in map(int, input().split()):
    a -= 1

    # 反転前の黒マスを減算
    now -= d[a] + d[a + 1]

    # マスの状態を反転
    d[a] ^= 1
    d[a + 1] ^= 1

    # 反転後の黒マスを加算
    now += d[a] + d[a + 1]

    # 黒マスの区間数
    print(now // 2)
