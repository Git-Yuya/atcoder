def find_min_domino(s_list: list[int]) -> int:
    """
    最小のドミノの個数を探索

    Args:
        s_list (list[int]): 各ドミノの大きさ

    Returns:
        min_domino (int): 最小のドミノの個数、または存在しない場合は-1
    """
    # 最小のドミノの個数
    min_domino = 2
    # 現在一番左のドミノの大きさ
    s_current = s_list[0]
    # ドミノnの大きさ
    s_n = s_list[-1]
    # ドミノの大きさリスト
    s_list = s_list[1:]
    s_list.sort()

    while 2 * s_current < s_n:
        # 倒れるドミノ候補の大きさ
        s_candidate_list = []
        # ドミノリスト更新のためのインデックス
        index = 0

        # 倒れるドミノ候補を探索
        for s in s_list:
            if s <= 2 * s_current:
                s_candidate_list.append(s)
                index += 1

        # 倒れるドミノがない場合
        if s_candidate_list == []:
            return -1

        # 倒れるドミノがある場合
        else:
            s_current = max(s_candidate_list)
            s_list = s_list[index:]
            min_domino += 1

    return min_domino


T = int(input())

for _ in range(T):
    N = int(input())
    S_list = list(map(int, input().split()))
    print(find_min_domino(S_list))


# ========== 別解 ==========
import io
import os

import bisect

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


def solve() -> None:
    N = int(input())
    arr = list(map(int, input().split()))

    # ドミノ1の大きさ
    left = arr[0]
    # ドミノNの大きさ
    right = arr[N - 1]

    # 両端以外のドミノの大きさリスト
    mid = arr[1:N - 1]
    mid.sort()

    # 直前に使ったインデックス
    loc = -1

    # 最小のドミノの個数
    ans = 2
    # 現在のドミノの大きさ
    curr = left

    while True:
        if 2 * curr >= right:
            break

        # 倒れるドミノの最大のmidのインデックス
        newloc = bisect.bisect(mid, 2 * curr) - 1

        # 倒れるドミノがない場合
        if newloc == loc:
            print(-1)
            return

        ans += 1
        curr = mid[newloc]
        loc = newloc

    print(ans)


T = int(input())

for _ in range(T):
    solve()
