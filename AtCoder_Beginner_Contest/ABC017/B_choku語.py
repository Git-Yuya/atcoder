X = input()

X = X.replace("ch", "").replace("o", "").replace("k", "").replace("u", "")

print("YES" if X == "" else "NO")
