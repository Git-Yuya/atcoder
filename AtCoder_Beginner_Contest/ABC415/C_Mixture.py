from collections import deque

T = int(input())

for _ in range(T):
    N = int(input())
    S = "0" + input()

    # 0から2^{N-1}までの状態の数
    all_state = 1 << N

    # 状態iが安全かどうか
    is_safe = [True] * all_state
    for i in range(1, all_state):
        if S[i] == "1":
            is_safe[i] = False

    # 各状態が既に訪問済みかどうか
    visited = [False] * all_state

    queue = deque()
    queue.append(0)
    visited[0] = True

    while queue:
        current_state = queue.popleft()

        for i in range(N):
            # 薬品iを注いでいない場合
            if not (current_state >> i) & 1:
                next_state = current_state | (1 << i)

                # 次の状態が安全で、まだ訪問していない場合
                if is_safe[next_state] and not visited[next_state]:
                    visited[next_state] = True
                    queue.append(next_state)

    print("Yes" if visited[all_state - 1] else "No")


# ========== 別解 ==========
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    S = input().rstrip()

    # 全ての薬品を注いだ状態のビットマスク
    full = (1 << N) - 1
    # dp[mask]: 状態maskが安全かどうか
    dp = [False] * (1 << N)
    # 何も注いでいない状態は安全
    dp[0] = True

    for mask in range(1, full + 1):
        # 状態maskが危険な場合
        if S[mask - 1] == "1":
            continue

        for j in range(N):
            # j番目の薬品が混ざっている場合
            if mask & (1 << j):
                # j番目の薬品を注いでいない状態が安全である場合
                if dp[mask ^ (1 << j)]:
                    dp[mask] = True
                    break

    print("Yes" if dp[full] else "No")
