x_a, y_a, x_b, y_b, x_c, y_c = map(int, input().split())

x_b -= x_a
y_b -= y_a
x_c -= x_a
y_c -= y_a

print(abs(x_b * y_c - x_c * y_b) / 2)
