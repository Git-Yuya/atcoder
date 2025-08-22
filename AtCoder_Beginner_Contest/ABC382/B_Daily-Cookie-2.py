N, D = map(int, input().split())
S = input()

S = S[::-1].replace("@", ".", D)

print(S[::-1])
