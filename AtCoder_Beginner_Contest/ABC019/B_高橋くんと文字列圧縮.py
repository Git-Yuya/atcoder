s = input()

current_c = s[0]
count = 1
result = ""

for c in s[1:]:
    if c == current_c:
        count += 1
    else:
        result += current_c + str(count)
        current_c = c
        count = 1
result += current_c + str(count)

print(result)
