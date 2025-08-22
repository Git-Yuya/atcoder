N = int(input())
S = input()

if N % 2 == 0:
    print("No")
else:
    for i, t in enumerate(S, start=1):
        if i <= (N + 1) // 2 - 1 and t != "1":
            print("No")
            break
        elif i == (N + 1) // 2 and t != "/":
            print("No")
            break
        elif i >= (N + 1) // 2 + 1 and t != "2":
            print("No")
            break
    else:
        print("Yes")
