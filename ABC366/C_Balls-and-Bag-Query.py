# 入力
Q = int(input())

# 袋に入っている数字カウント
count = {}
# 袋に入っている数字の種類
number = 0

for i in range(Q):
    query_type, *x = map(int, input().split())
    
    if query_type == 1:
        if x[0] in count:
            if count[x[0]] == 0:
                number += 1
            count[x[0]] += 1
        else:
            count[x[0]] = 1
            number += 1
    
    elif query_type == 2:
        count[x[0]] -= 1
        if count[x[0]] == 0:
            number -= 1
    
    else:
        print(number)




##### 別解 #####
# from collections import defaultdict


# def c_balls_and_bag_query():
#     # 入力
#     Q = int(input())
#     Queries = [[int(col) for col in input().split()] for row in range(Q)]

#     # ボールの数をカウントする辞書、デフォルト値は0
#     bag = defaultdict(int)
#     # 結果
#     ans = []
    
#     for q in Queries:
#         type = q[0]
#         match type:
#             case 1:
#                 x = q[1]
#                 bag[x] += 1
#             case 2:
#                 x = q[1]
#                 bag[x] -= 1
#                 if bag[x] == 0:
#                     del bag[x]
#             case 3:
#                 ans.append(len(bag))
#             case _:
#                 pass
    
#     # ansを改行で結合
#     return "\n".join(map(str, ans))


# print(c_balls_and_bag_query())
