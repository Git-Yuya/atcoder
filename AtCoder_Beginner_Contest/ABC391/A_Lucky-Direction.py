D = input()

for c in D:
    if c == "N":
        print("S", end="")
    elif c == "S":
        print("N", end="")
    elif c == "E":
        print("W", end="")
    elif c == "W":
        print("E", end="")
