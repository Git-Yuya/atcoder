def count_snake_numbers(num: int) -> int:
    """
    num以下のヘビ数を求める

    Args:
        num (int): 対象の整数

    Returns:
        res (int): num以下のヘビ数
    """
    s = str(num)
    n = len(s)
    digit_list = [int(d) for d in s]

    res = 0

    # numと同じ桁数で、先頭の数字も同じである数を数え上げ
    for i in range(1, n + 1):
        if i == n:
            res += 1
            break

        res += (digit_list[0] ** (n - 1 - i)) * min(digit_list[0], digit_list[i])

        if digit_list[i] >= digit_list[0]:
            break

    # numより桁数が少ない数、または、numと同じ桁数で先頭の数字が小さい数を数え上げ
    for i in range(n):
        # 先頭の数字の最大値
        head_max = 9 if i else digit_list[0] - 1

        for j in range(1, head_max + 1):
            res += j ** (n - 1 - i)

    return res


L, R = map(int, input().split())

print(count_snake_numbers(R) - count_snake_numbers(L - 1))
