S = input()
T = input()

for i in range(max(len(S), len(T))):
    if i >= len(S):
        print(i + 1)
        break
    elif i >= len(T):
        print(i + 1)
        break
    
    if S[i] != T[i]:
        print(i + 1)
        break

else:
    print(0)
