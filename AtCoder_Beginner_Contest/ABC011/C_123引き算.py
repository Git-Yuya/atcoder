N = int(input())
NG = [int(input()) for _ in range(3)]

is_ok = True
count = 0

while N > 0:
    if N in NG:
        is_ok = False
        break

    if N - 3 not in NG:
        N -= 3
    elif N - 2 not in NG:
        N -= 2
    elif N - 1 not in NG:
        N -= 1
    else:
        is_ok = False
        break

    count += 1

if count > 100 or not is_ok:
    print("NO")
else:
    print("YES")
