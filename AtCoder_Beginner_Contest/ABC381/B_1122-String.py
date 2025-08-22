S = input()

if len(S) % 2 == 0:
    for i in range(0, len(S), 2):
        if S.count(S[i]) != 2 or S[i] != S[i + 1]:
            print("No")
            break
    else:
        print("Yes")
else:
    print("No")
