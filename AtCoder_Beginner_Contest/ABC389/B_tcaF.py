X = int(input())

current_value = 1
for num in range(1, X + 1):
    current_value *= num
    if current_value == X:
        print(num)
        break
