N = int(input())

# 感雨時刻のリスト
rain_times = []

for _ in range(N):
    S, E = map(int, input().split("-"))

    # 降り始めは直前の5分単位に切り下げ
    S = (S // 5) * 5
    # 降り終わりは直後の5分単位に切り上げ
    E = ((E + 4) // 5) * 5

    # 切り上げで下2桁が60になった場合は次の時間に繰り上げ
    if E % 100 == 60:
        E += 40

    rain_times.append((S, E))

# 開始時刻でソート
rain_times.sort()

# 連続する時間帯を結合
merged_rain_times = []
current_start, current_end = rain_times[0]

for start, end in rain_times[1:]:
    # 時間帯が重なる場合
    if start <= current_end:
        current_end = max(current_end, end)
    # 時間帯が重ならない場合
    else:
        merged_rain_times.append((current_start, current_end))
        current_start, current_end = start, end
merged_rain_times.append((current_start, current_end))

for start, end in merged_rain_times:
    print(f"{start:04d}-{end:04d}")
