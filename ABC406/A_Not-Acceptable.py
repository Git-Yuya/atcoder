A, B, C, D = map(int, input().split())

if C < A:
    print("Yes")
elif C == A and D < B:
    print("Yes")
else:
    print("No")


# ========== 別解 ==========
A, B, C, D = map(int, input().split())

# 秒数
deadline = A * 60 + B
submission = C * 60 + D

print("Yes" if submission < deadline else "No")
