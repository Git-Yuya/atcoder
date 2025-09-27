A = int(input())
B = int(input())
C = int(input())

rank = sorted([A, B, C], reverse=True)

print(rank.index(A) + 1)
print(rank.index(B) + 1)
print(rank.index(C) + 1)
