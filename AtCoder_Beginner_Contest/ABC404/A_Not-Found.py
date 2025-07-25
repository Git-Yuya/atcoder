S = input()

lowercase = "abcdefghijklmnopqrstuvwxyz"

for c in lowercase:
    if c not in S:
        print(c)
        break
