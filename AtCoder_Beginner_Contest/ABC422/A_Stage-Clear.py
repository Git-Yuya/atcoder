S = input()

i = int(S[0])
j = int(S[2])

if j < 8:
    print(f"{i}-{j + 1}")
elif j == 8:
    print(f"{i + 1}-1")
