def list_divisors(n):
    """ nの約数を列挙 """
    lower_divisors , upper_divisors = [], []

    i = 1
    while i ** 2 <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1

    return lower_divisors + upper_divisors[::-1]


N, K = map(int,input().split())
MOD = 10 ** 9 + 7

k_divisors = list_divisors(K)
sum_by_divisors = [0] * len(k_divisors)
ans = 0

# 約数を大きい方から取り出す
for i in range(len(k_divisors) - 1, -1, -1):
    kd = k_divisors[i]

    # N以下の最大のkdの倍数を取得
    max_val = (N // kd) * kd
    # N以下のkdの倍数の和(kd 〜 max_valまでの等差数列の和)
    # LCM(ax, K) = aK より
    # ax + 2ax + 3ax + ... = x(a + 2a + 3a + ...) という形の和が求まる
    sum_by_divisors[i] = (kd + max_val) * (N // kd) // 2

    # 約数を大きい順に回しているので、今操作している約数より大きい約数に対してだけ処理
    for j in range(i + 1, len(k_divisors)):
        if k_divisors[j] % kd == 0:
            # 今まで出てきた約数でkdの倍数があれば重複カウントしているためマイナス
            sum_by_divisors[i] -= sum_by_divisors[j]

    # ax + 2ax + 3ax + ... = x(a + 2a + 3a + ...) という形の和が求まっているので約数xで割る
    ans += sum_by_divisors[i] // kd
    ans %= MOD

# ansにはa + 2a + 3a + ...形の総和が格納されている
# 求めたいのは LCM(ax, K) = aK の aK の和なので最後にKをかける
ans *= K
ans %= MOD

print(ans)
