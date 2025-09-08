T = int(input())

for _ in range(T):
    n_A, n_B, n_C = map(int, input().split())

    # コンテストの開催数
    count = 0

    # ACのペア数
    if n_A < n_C:
        pair_AC = n_A
        n_A = 0
        n_C -= pair_AC
    else:
        pair_AC = n_C
        n_C = 0
        n_A -= pair_AC

    # ACのペアとBを使って、ABCのコンテストを開催
    if pair_AC > n_B:
        count_ABC = n_B
        pair_AC -= n_B
    else:
        count_ABC = pair_AC
        pair_AC = 0
    count += count_ABC

    # ACのペアとAを使って、AACのコンテストを開催
    count_AAC = min(pair_AC, n_A)
    pair_AC -= count_AAC
    count += count_AAC

    # ACのペアとCを使って、ACCのコンテストを開催
    count_ACC = min(pair_AC, n_C)
    pair_AC -= count_ACC
    count += count_ACC

    # 残りのACのペアを使って、AACかACCのコンテストを開催
    quotient = pair_AC // 3
    if pair_AC % 3 == 0:
        count += quotient * 2
    elif pair_AC % 3 == 1:
        count += quotient * 2
    else:
        count += quotient * 2 + 1

    print(count)


# ========== 別解 ==========
T = int(input())

for _ in range(T):
    n_A, n_B, n_C = map(int, input().split())

    print(min(n_A, n_C, (n_A + n_B + n_C) // 3))
