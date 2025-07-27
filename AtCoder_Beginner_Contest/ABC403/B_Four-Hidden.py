T = input()
U = input()

# SがUを連続部分文字列として含んでいた可能性があるかどうか
is_same = False

for i in range(len(T) - len(U) + 1):
    for j in range(len(U)):
        if T[i + j] == U[j] or T[i + j] == "?":
            # Uの最後の文字まで一致した場合
            if j == len(U) - 1:
                is_same = True
                break
        else:
            break

print("Yes" if is_same else "No")


# ========== 別解 ==========
T = list(input())
U = list(input())

for i in range(len(T) - len(U) + 1):
    for j in range(len(U)):
        if T[i + j] != U[j] and T[i + j] != "?":
            break
    else:
        print("Yes")
        exit()

print("No")
