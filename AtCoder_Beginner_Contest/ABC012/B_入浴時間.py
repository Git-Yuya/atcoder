N = int(input())

hh = N // 3600
mm = (N % 3600) // 60
ss = N % 60

print(f"{hh:02}:{mm:02}:{ss:02}")
