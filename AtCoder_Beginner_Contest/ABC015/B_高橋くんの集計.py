N = int(input())
A = list(map(int, input().split()))

bug_sum = 0
bug_len = 0

for a in A:
    if a == 0:
        continue
    bug_sum += a
    bug_len += 1

print((bug_sum - 1) // bug_len + 1)
