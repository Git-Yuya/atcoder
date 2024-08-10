import itertools

# 入力
N = int(input())


def check(c_list: list[str]) -> bool:
    """
    正しいカッコ列であるかを判定する関数
    
    Args:
        c_list (list[str]): 文字列Sの文字リスト
    
    Returns:
        bool: 正しいカッコ列ならTrue、そうでなければFalse
    """
    # "("の数 - ")"の数
    diff = 0
    
    for c in c_list:
        if c == "(":
            diff += 1
        else:
            diff -= 1
            if diff < 0:
                return False
    
    return diff == 0


# Nが偶数である場合
if N % 2 == 0:
    for S in itertools.product(["(", ")"], repeat=N):
        if check(list(S)):
            # 出力
            print("".join(S))




##### 別解 #####
# # 入力
# N = int(input())

# # Nが偶数でない場合
# if N % 2 == 1:
#     exit()

# # 括弧の対の数
# N //= 2

# # 集合のリストを作成
# # ls[i]: i組の括弧で作ることができるすべての有効な括弧の組み合わせを格納する集合
# ls = [set() for _ in range(N + 1)]
# # 0組の括弧では、空文字列のみが有効な組み合わせ
# ls[0].add("")

# # 1組からN組の括弧に対して有効な組み合わせを作成
# for i in range(1, N + 1):
#     # i-1組の括弧からi組の括弧を作成
#     for s in ls[i - 1]:
#         # i-1組の括弧から、括弧のペアで囲むことでi組の括弧を作成
#         ls[i].add("(" + s + ")")
    
#     # a組の括弧とb組の括弧を連結してi組の括弧を作成
#     for a in range(1, i):
#         # b組の括弧の数
#         b = i - a
#         # a組の括弧のすべての組み合わせ
#         for s1 in ls[a]:
#             # b組の括弧のすべての組み合わせ
#             for s2 in ls[b]:
#                 # a組とb組を連結してi組の括弧を作成
#                 ls[i].add(s1 + s2)
    
# # N組の括弧のすべての組み合わせを辞書順にソートし、リストに変換
# ans = sorted(list(ls[N]))

# # 出力
# for s in ans:
#   print(s)
