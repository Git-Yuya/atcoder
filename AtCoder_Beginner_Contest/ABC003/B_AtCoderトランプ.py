S = input()
T = input()

is_same = True

for i in range(len(S)):
    if S[i] != T[i]:
        if S[i] == "@" and T[i] in "atcoder":
            continue
        elif T[i] == "@" and S[i] in "atcoder":
            continue
        else:
            is_same = False
            break

print("You can win" if is_same else "You will lose")
