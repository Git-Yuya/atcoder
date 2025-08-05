N, L, R = map(int, input().split())
S = input()

if "x" in S[L - 1:R]:
    print("No")
else:
    print("Yes")
