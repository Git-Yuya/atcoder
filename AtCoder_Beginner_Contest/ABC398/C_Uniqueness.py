from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

# 各番号を持つ人
count = defaultdict(list)
for i, a in enumerate(A):
    count[a].append(i)

# 持っている番号で降順にソート
sorted_count = sorted(count.items(), key=lambda x: x[0], reverse=True)

for num, person_list in sorted_count:
    if len(person_list) == 1:
        print(person_list[0] + 1)
        break

else:
    print(-1)


# ========== 別解 ==========
from collections import Counter

N = input()
A = list(map(int, input().split()))

c = Counter(A)
unique_numbers = [k for k, v in c.items() if v == 1]

if len(unique_numbers) == 0:
    print(-1)
else:
    max_unique = max(unique_numbers)
    print(A.index(max_unique) + 1)
