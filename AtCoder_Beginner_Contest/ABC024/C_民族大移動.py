N, D, K = map(int, input().split())
L_list, R_list = [], []
for _ in range(D):
    L, R = map(int, input().split())
    L_list.append(L)
    R_list.append(R)
S_list, T_list = [], []
for _ in range(K):
    S, T = map(int, input().split())
    S_list.append(S)
    T_list.append(T)

# 各部族の移動日数
moving_days = [0] * K

for i in range(D):
    L = L_list[i]
    R = R_list[i]

    for j in range(K):
        # まだ目的地に到達していない場合
        if moving_days[j] == 0:
            # 現在地が移動可能区間にある場合
            if L <= S_list[j] <= R:
                # 目的地も移動可能区間にある場合
                if L <= T_list[j] <= R:
                    moving_days[j] = i + 1
                # 目的地が移動可能区間にない場合
                else:
                    # 現在地から目的地に向かって移動
                    if S_list[j] < T_list[j]:
                        S_list[j] = R
                    else:
                        S_list[j] = L

for days in moving_days:
    print(days)
