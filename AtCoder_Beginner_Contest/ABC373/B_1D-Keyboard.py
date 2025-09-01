S = input()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
current_x = S.index("A")
moving_distance = 0

for char in alphabet:
    target_x = S.index(char)
    moving_distance += abs(target_x - current_x)
    current_x = target_x

print(moving_distance)
