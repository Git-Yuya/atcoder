H, W, X, Y = map(int, input().split())
S = [input() for _ in range(H)]
T = input()

current_x, current_y = X - 1, Y - 1
passed_houses = set()

for i in range(len(T)):
    if T[i] == "U" and S[current_x - 1][current_y] != "#":
        if S[current_x - 1][current_y] == "@":
            passed_houses.add((current_x - 1, current_y))
        current_x -= 1
    elif T[i] == "D" and S[current_x + 1][current_y] != "#":
        if S[current_x + 1][current_y] == "@":
            passed_houses.add((current_x + 1, current_y))
        current_x += 1
    elif T[i] == "L" and S[current_x][current_y - 1] != "#":
        if S[current_x][current_y - 1] == "@":
            passed_houses.add((current_x, current_y - 1))
        current_y -= 1
    elif T[i] == "R" and S[current_x][current_y + 1] != "#":
        if S[current_x][current_y + 1] == "@":
            passed_houses.add((current_x, current_y + 1))
        current_y += 1
    else:
        pass

print(current_x + 1, current_y + 1, len(passed_houses))


# ========== 別解 ==========
H, W, X, Y = map(int, input().split())
S = [list(input()) for _ in range(H)]
T = input()

current_x, current_y = X - 1, Y - 1
C = 0

for t in T:
    if t == "U" and S[current_x - 1][current_y] != "#":
        current_x -= 1
        if S[current_x][current_y] == "@":
            C += 1
            S[current_x][current_y] = "."
    elif t == "D" and S[current_x + 1][current_y] != "#":
        current_x += 1
        if S[current_x][current_y] == "@":
            C += 1
            S[current_x][current_y] = "."
    elif t == "L" and S[current_x][current_y - 1] != "#":
        current_y -= 1
        if S[current_x][current_y] == "@":
            C += 1
            S[current_x][current_y] = "."
    elif t == "R" and S[current_x][current_y + 1] != "#":
        current_y += 1
        if S[current_x][current_y] == "@":
            C += 1
            S[current_x][current_y] = "."

print(current_x + 1, current_y + 1, C)
