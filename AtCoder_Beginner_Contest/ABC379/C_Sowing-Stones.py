N, M = map(int, input().split())
X = list(map(int, input().split()))
A = list(map(int, input().split()))

XA = []
for i in range(M):
    XA.append((X[i], A[i]))
XA = sorted(XA, key=lambda x: x[0])

if sum(A) != N:
    print(-1)
    exit()

# 現在の石の合計
current_stones = 0
# マス0から移動させたと仮定した時、ある位置までの石の移動回数
moving_stones = 0

for x, a in XA:
    # 現在の石の合計がマスの位置よりも少ない場合
    if current_stones < x - 1:
        print(-1)
        exit()

    current_stones += a
    moving_stones += x * a

print(N * (N + 1) // 2 - moving_stones)
