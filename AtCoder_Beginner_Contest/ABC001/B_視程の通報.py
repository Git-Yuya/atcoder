m = int(input())

# キロ表記
k = m / 1000

if k < 0.1:
    print("00")
elif k <= 5:
    print(f"{int(k * 10):02d}")
elif k <= 30:
    print(f"{int(k) + 50:02d}")
elif k <= 70:
    print(f"{(int(k) - 30) // 5 + 80:02d}")
else:
    print("89")
