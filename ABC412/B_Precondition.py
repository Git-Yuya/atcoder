S = input()
T = input()

# Sの先頭でない大文字の前の文字リスト
c_list = []
for i in range(1, len(S)):
    if S[i].isupper():
        c_list.append(S[i - 1])

# c_listがすべてTに含まれているかどうか
is_included = True
for c in c_list:
    if c not in T:
        is_included = False

print("Yes" if is_included else "No")


# ========== 別解 ==========
S = input()
T = input()

for i in range(len(S) - 1):
    if S[i + 1].isupper():
        if S[i] not in T:
            print("No")
        break
else:
    print("Yes")
