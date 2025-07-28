N = int(input())

# ログインしているか
is_logged_in = False
# 認証エラーの回数
auth_error_count = 0

for _ in range(N):
    S = input()

    if S == "login":
        is_logged_in = True

    elif S == "logout":
        is_logged_in = False

    elif S == "public":
        continue

    elif S == "private":
        if not is_logged_in:
            auth_error_count += 1

print(auth_error_count)
