S_AB, S_AC, S_BC = input().split()

if S_AB == "<":
    if S_AC == "<":
        if S_BC == "<":
            print("B")
        else:
            print("C")
    else:
        print("A")
else:
    if S_AC == "<":
        print("A")
    else:
        if S_BC == "<":
            print("C")
        else:
            print("B")


# ========== 別解 ==========
S_AB, S_AC, S_BC = input().split()

if S_AB == S_BC:
    print("B")
elif S_AB == S_AC:
    print("C")
else:
    print("A")
