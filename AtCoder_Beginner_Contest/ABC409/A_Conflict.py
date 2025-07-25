N = int(input())
T = input()
A = input()

# 2人とも同じ商品が欲しいかどうか
is_same = False

for i in range(N):
    if T[i] == "o" and A[i] == "o":
        is_same = True
        break

print("Yes" if is_same else "No")
