from collections import defaultdict

N = int(input())
S = [input() for _ in range(N)]

result = defaultdict(int)
for s in S:
    result[s] += 1

max_votes = max(result.values())
winners = [k for k, v in result.items() if v == max_votes]

print(winners[0])
