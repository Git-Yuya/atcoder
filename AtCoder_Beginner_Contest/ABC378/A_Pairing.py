A1, A2, A3, A4 = map(int, input().split())

if A1 == A2:
    if A3 == A4:
        print(2)
    else:
        print(1)
elif A1 == A3:
    if A2 == A4:
        print(2)
    else:
        print(1)
elif A1 == A4:
    if A2 == A3:
        print(2)
    else:
        print(1)
elif A2 == A3:
    print(1)
elif A2 == A4:
    print(1)
elif A3 == A4:
    print(1)
else:
    print(0)


# ========== 別解 ==========
A = list(map(int, input().split()))

ans = 0
while len(A) > 0:
    x = A.pop()
    if x in A:
        ans += 1
        A.remove(x)

print(ans)
