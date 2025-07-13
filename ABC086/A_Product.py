a, b = map(int, input().split())

# aとbのどちらかが2の倍数であればabは偶数
if (a % 2 == 0) or (b % 2 == 0):
    print("Even")
else:
    print("Odd")


# ========== 別解 ==========
a, b = map(int, input().split())

# abが2の倍数であれば偶数
if (a * b) % 2 == 0:
    print("Even")
else:
    print("Odd")
