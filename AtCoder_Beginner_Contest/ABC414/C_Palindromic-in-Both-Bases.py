def generate_palindromes(n: int) -> list[int]:
    """
    1以上n以下の整数の内、10進数で回文になるものを効率的に生成

    Args:
        n (int): 生成する回文の上限

    Returns:
        palindromes (list[int]): 生成された回文のリスト
    """
    palindromes = []

    # 1桁の回文
    for i in range(1, min(10, n + 1)):
        palindromes.append(i)

    # 2桁以上の回文
    digits = 2
    while True:
        # digits桁の最小の数が n を超えたら終了
        if 10 ** (digits - 1) > n:
            break

        # 上半分の桁数を計算
        half_digits = (digits + 1) // 2

        # 上半分の開始値と終了値
        start = 10 ** (half_digits - 1)
        end = 10 ** half_digits

        for i in range(start, end):
            s = str(i)

            # 偶数桁の場合は上半分をそのまま反転
            if digits % 2 == 0:
                palindrome = int(s + s[::-1])

            # 奇数桁の場合は最後の1文字を除いて反転
            else:
                palindrome = int(s + s[-2::-1])

            if palindrome > n:
                break
            palindromes.append(palindrome)

        digits += 1

    return palindromes


def is_palindrome(a: int, n: int) -> bool:
    """
    A進法で表現したときに回文かどうかを判定

    Args:
        a (int): 進法
        n (int): 判定する整数

    Returns:
        bool: 回文ならTrue, そうでなければFalse
    """
    if a == 10:
        s = str(n)
        return s == s[::-1]

    s = ""
    while n > 0:
        s += str(n % a)
        n //= a

    return s == s[::-1]


A = int(input())
N = int(input())

# 回文であるものの総和
sum = 0
# 10進数で回文になる数を生成
decimal_palindromes = generate_palindromes(N)

for num in decimal_palindromes:
    if is_palindrome(A, num):
        sum += num

print(sum)


# ========== 別解 ==========
import math


def base_n_check_palindrome(num: int, base: int) -> bool:
    """
    指定された進法で表現したときに回文かどうかを判定

    Args:
        num (int): 判定する整数
        base (int): 進法

    Returns:
        status (bool): 回文ならTrue, そうでなければFalse
    """
    status = True
    digit = math.floor(math.log(num, base)) + 1
    num_1, num_2 = num, num

    for i in range(digit - 1, -1, -1):
        if (num_1 // base ** (i)) != (num_2 % base):
            status = False
            return status
        num_1 %= base ** (i)
        num_2 //= base

    return status


A = int(input())
N = int(input())

total = 0
digit = len(str(N))

for i in range(1, 10 ** ((digit + 1) // 2) + 1):
    # 偶数桁の回文
    num = int(str(i) + str(i)[::-1])
    if num <= N:
        if base_n_check_palindrome(num, A):
            total += num

    # 奇数桁の回文
    num = int(str(i)[:-1] + str(i)[::-1])
    if num <= N:
        if base_n_check_palindrome(num, A):
            total += num

print(total)
