A, B = map(int, input().split())

x_set = set()

# (A, B, x), (x, B, A)
x_set.add(2 * B - A)
# (A, x, B), (B, x, A)
if (A + B) % 2 == 0:
    x_set.add((A + B) // 2)
# (B, A, x), (x, A, B)
x_set.add(2 * A - B)

print(len(x_set))
