N, c1, c2 = input().split()
S = input()

for s in S:
    if s == c1:
        print(s, end="")
    else:
        print(c2, end="")
