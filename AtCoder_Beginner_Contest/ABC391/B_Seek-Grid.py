N, M = map(int, input().split())
S = [list(input().strip()) for _ in range(N)]
T = [list(input().strip()) for _ in range(M)]

for a in range(N - M + 1):
    for b in range(N - M + 1):
        for i in range(M):
            for j in range(M):
                if S[a + i][b + j] != T[i][j]:
                    break

            # 内側のfor(j)がbreakされなければ次のiへ
            else:
                continue
            # breakされた場合は次の(a, b)へ
            break

        # すべて一致した場合
        else:
            print(a + 1, b + 1)
            exit()


# ========== 別解 ==========
N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]

for i in range(N - M + 1):
    for j in range(N - M + 1):
        for p in range(M):
            flag = True
            if S[i+p][j:j+M] != T[p]:
                flag = False
                break
        if flag:
            print(i + 1, j + 1)
            exit(0)
