N = int(input())

# ランレングス圧縮前の文字列
S = ""

for _ in range(N):
    c, l = map(str, input().split())

    if (len(S) + int(l)) > 100:
        S = "Too Long"
        break

    S += c * int(l)

print(S)


# ========== 別解 ==========
N = int(input())
A = []
for _ in range(N):
    A.append(list(map(str, input().split())))

S = []
count = 0

for i in A:
    count += int(i[1])
    if count <= 100:
        S.append(i[0] * int(i[1]))
    else:
        print("Too Long")
        break

if count <= 100:
    print("".join(S))
