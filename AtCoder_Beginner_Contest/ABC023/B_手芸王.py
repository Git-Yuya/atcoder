N = int(input())
S = input()

if N % 2 == 0:
    print(-1)

else:
    current_S = "b"

    for i in range(N // 2):
        if i % 3 == 0:
            current_S = "a" + current_S + "c"
        elif i % 3 == 1:
            current_S = "c" + current_S + "a"
        else:
            current_S = "b" + current_S + "b"

    if current_S == S:
        print(N // 2)
    else:
        print(-1)
