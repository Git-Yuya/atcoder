A = input()

if A == "a":
    print(-1)
elif len(A) == 1:
    print("a")
else:
    print("a" * (len(A) - 1))
