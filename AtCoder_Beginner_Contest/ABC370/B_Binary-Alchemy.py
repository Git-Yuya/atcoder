from collections import defaultdict

N = int(input())
A_dict = defaultdict(int)
for i in range(N):
    A_list = list(map(int, input().split()))
    for j in range(i + 1):
        A_dict[(i + 1, j + 1)] = A_list[j]

# 現在の元素
current_element = 1

for j in range(1, N + 1):
    if current_element >= j:
        current_element = A_dict[(current_element, j)]
    else:
        current_element = A_dict[(j, current_element)]

print(current_element)
