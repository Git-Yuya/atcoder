S = input()

print(len(S.replace("io", "")))


# ========== 別解 ==========
S = input()

io = S.count("io") * 2
print(len(S) - io)
