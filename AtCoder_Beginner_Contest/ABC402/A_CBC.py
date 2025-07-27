S = input()

for c in S:
    if "A" <= c <= "Z":
        print(c, end="")


# ========== 別解 ==========
S = input()

ans = ""
for c in S:
    if c.isupper():
        ans += c

print(ans)
