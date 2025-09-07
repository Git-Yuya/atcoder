X = input()

while True:
    if X[-1] == "0":
        X = X[:-1]
    else:
        break

if X[-1] == ".":
    X = X[:-1]

print("".join(X))


# ========== 別解 ==========
X = float(input())

if int(X) == X:
    print(int(X))
else:
    print(X)


# ========== 別解 ==========
X = input().rstrip("0")

if X.endswith("."):
    X = X.rstrip(".")

print(X)
