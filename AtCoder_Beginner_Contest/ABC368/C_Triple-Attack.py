N = int(input())
H = list(map(int, input().split()))

T = 1

for i in range(N):
    # H[i]が5以上の場合
    if H[i] >= 5:
        quotient = H[i] // 5
        H[i] -= quotient * 5
        T += quotient * 3

    # H[i]は4以下
    while H[i] >= 1:
        if T % 3 == 0:
            H[i] -= 3
        else:
            H[i] -= 1
        T += 1

print(T - 1)
