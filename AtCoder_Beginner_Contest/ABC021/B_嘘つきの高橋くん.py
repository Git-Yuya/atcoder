N = int(input())
a, b = map(int, input().split())
K = int(input())
P = list(map(int, input().split()))

visited = set()
visited.add(a)
visited.add(b)

for p in P:
    if p in visited:
        print("NO")
        break
    visited.add(p)

else:
    print("YES")
