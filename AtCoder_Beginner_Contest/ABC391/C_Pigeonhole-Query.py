N, Q = map(int, input().split())

# 鳩がどの巣にいるか
pigeon_pos = [i for i in range(N)]
# 各巣に鳩が何羽いるか
nest_count = [1] * N
# 複数の鳩がいる巣の個数
count = 0

for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        P, H = query[1] - 1, query[2] - 1
        # 鳩が元々いた巣
        prev_pos = pigeon_pos[P]
        nest_count[prev_pos] -= 1
        if nest_count[prev_pos] == 1:
            count -= 1

        # 鳩の移動先の巣
        pigeon_pos[P] = H
        nest_count[H] += 1
        if nest_count[H] == 2:
            count += 1

    elif query[0] == 2:
        print(count)
