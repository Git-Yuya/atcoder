N = int(input())

baroon = []
for _ in range(N):
    H, S = map(int, input().split())
    baroon.append((H, S))

def is_ok(val):
    """ val秒後に全てのバルーンを割れるか判定する関数 """
    # 各秒ごとに割れるバルーンの数を管理
    cnt = [0] * (N + 1)

    for i in range(N):
        if val < baroon[i][0]:
            # val秒後でも割れないバルーンがある場合はFalse
            return False
        # バルーンiを割るまでに必要な秒数を計算し、cntに加算
        cnt[min((val - baroon[i][0]) // baroon[i][1], N)] += 1

    for i in range(N):
        if cnt[i] > i + 1:
            # i秒までに割れるバルーンの数がi+1を超える場合はFalse
            return False
        if i != N - 1:
            # 次の秒にバルーンの数を繰り越す
            cnt[i + 1] += cnt[i]

    return True

left = 0
right = 10 ** 18

# 二分探索
while left < right:
    mid = (left + right) // 2
    if is_ok(mid):
        right = mid
    else:
        left = mid + 1

print(left)
