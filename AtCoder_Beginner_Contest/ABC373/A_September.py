S = [input() for _ in range(12)]

print(sum(1 for i in range(12) if len(S[i]) == i + 1))
