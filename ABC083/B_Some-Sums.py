# 入力
N, A, B = map(int, input().split())

# 総和
sum_total = 0

# 総和を計算
for i in range(1, N + 1):
    digit_list = list(str(i))
    digit_sum = 0
    for digit in digit_list:
        digit_sum += int(digit)
    if A <= digit_sum <= B:
        sum_total += i

# 出力
print(sum_total)




##### 別解 #####
# def calc_digit_sum(n: int) -> int:
#     """
#     各桁の和を計算する関数
    
#     Args:
#         n (int): 整数
    
#     Returns:
#         digit_sum (int): 各桁の和
#     """
#     digit_sum = 0
#     while n > 0:
#         digit_sum += n % 10
#         n //= 10

#     return digit_sum


# # 入力
# N, A, B = map(int, input().split())

# # 総和
# sum_total = 0

# # 総和を計算
# for i in range(1, N + 1):
#     if A <= calc_digit_sum(i) <= B:
#         sum_total += i

# # 出力
# print(sum_total)
