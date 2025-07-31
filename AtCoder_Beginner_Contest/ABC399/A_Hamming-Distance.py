N = int(input())
S = input()
T = input()

hamming_distance = sum(1 for i in range(N) if S[i] != T[i])
print(hamming_distance)
