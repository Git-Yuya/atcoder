a = int(input())
b = int(input())

print(abs(b - a) if abs(b - a) <= 5 else 10 - abs(b - a))
