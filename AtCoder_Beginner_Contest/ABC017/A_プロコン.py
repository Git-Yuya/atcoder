total_score = 0

for i in range(3):
    s, e = map(int, input().split())

    total_score += s * e * 0.1

print(int(total_score))
