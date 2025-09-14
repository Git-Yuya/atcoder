from bisect import bisect_left

N = int(input())
c = [int(input()) for _ in range(N)]

# 最長増加部分列
lis_dp = []

for c_i in c:
    idx = bisect_left(lis_dp, c_i)
    if idx == len(lis_dp):
        lis_dp.append(c_i)
    else:
        lis_dp[idx] = c_i

print(N - len(lis_dp))
