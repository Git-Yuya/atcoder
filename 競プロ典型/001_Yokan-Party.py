# 入力
N, L = map(int, input().split())
K = int(input())
A = [0] + list(map(int, input().split())) + [L]


def check(x: int) -> bool:
    """
    スコアがx以上になるかどうかを判定する関数
    
    Args:
        x: 閾値
        
    Returns
        bool: スコアがx以上ならTrue、そうでなければFalse
    """
    # 切れ目の数
    count = 0
    # 1切れの長さ
    length = 0
    
    # 左から順に長さがx以上になったら切る
    for i in range(N + 1):
        length += A[i + 1] - A[i]
        if length >= x:
            count += 1
            length = 0
    
    # 切れ目の数を判定
    if count >= K + 1:
        return True
    else:
        return False


# 二分探索
left = 0
right = L
while right - left > 1:
    mid = (left + right) // 2
    if check(mid):
        left = mid
    else:
        right = mid

# 出力
print(left)




##### 別解 #####
# # 入力
# N, L = map(int, input().split())
# K = int(input())
# A = list(map(int, input().split())) + [L]


# def can_divide_by(min_cut_len: int) -> bool:
#     """
#     スコアがmin_cut_len以上になるかどうかを判定する関数
    
#     Args:
#         x: 閾値
        
#     Returns
#         bool: スコアがmin_cut_len以上ならTrue、そうでなければFalse
#     """
#     # 切れ目の数
#     cut_count = 0
#     # 一つ前の切れ目の位置
#     pre_cut_pos = 0
    
#     for a in A:
#         if a - pre_cut_pos < min_cut_len:
#             continue

#         cut_count += 1
#         pre_cut_pos = a

#     return cut_count >= K + 1


# # 切れ目の長さの下限と上限
# lower_min_cut_len = 1
# upper_min_cut_len = L // (K + 1)

# while lower_min_cut_len < upper_min_cut_len:
#     middle_min_cut_len = (upper_min_cut_len + lower_min_cut_len) // 2 + 1

#     if can_divide_by(middle_min_cut_len):
#         lower_min_cut_len = middle_min_cut_len
#     else:
#         upper_min_cut_len = middle_min_cut_len - 1

# # 出力
# print(lower_min_cut_len)
