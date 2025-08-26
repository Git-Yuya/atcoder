N = int(input())
q_list, r_list = [], []
for _ in range(N):
    q, r = map(int, input().split())
    q_list.append(q)
    r_list.append(r)
Q = int(input())

for _ in range(Q):
    t, d = map(int, input().split())
    q, r = q_list[t - 1], r_list[t - 1]

    # d日より前に何回ゴミ収集日があるか
    count = ((d + q - r - 1) // q)
    # 次にゴミ収集車が来る日
    collection_day = r + q * count
    print(collection_day)
