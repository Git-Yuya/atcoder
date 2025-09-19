tx_a, ty_a, tx_b, ty_b, T, V = map(int, input().split())
n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]

for i in range(n):
    x, y = xy[i]
    d1 = ((tx_a - x) ** 2 + (ty_a - y) ** 2) ** 0.5
    d2 = ((tx_b - x) ** 2 + (ty_b - y) ** 2) ** 0.5

    if d1 + d2 <= T * V:
        print("YES")
        break

else:
    print("NO")
