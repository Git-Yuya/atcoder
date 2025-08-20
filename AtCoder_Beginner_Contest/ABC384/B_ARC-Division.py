N, R = map(int, input().split())

current_rating = R

for _ in range(N):
    D, A = map(int, input().split())

    if D == 1 and (1600 <= current_rating <= 2799):
        current_rating += A
    elif D == 2 and (1200 <= current_rating <= 2399):
        current_rating += A

print(current_rating)
