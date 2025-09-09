from decimal import ROUND_HALF_UP, Decimal

Deg, Dis = map(int, input().split())
Deg = Deg / 10

# 風速
wind_speed = Decimal(Dis) / Decimal(60)
wind_speed = wind_speed.quantize(Decimal("0.1"), ROUND_HALF_UP)
wind_speed = float(wind_speed)

# 風力
if (0.0 <= wind_speed <= 0.2):
    W = 0
elif (0.3 <= wind_speed <= 1.5):
    W = 1
elif (1.6 <= wind_speed <= 3.3):
    W = 2
elif (3.4 <= wind_speed <= 5.4):
    W = 3
elif (5.5 <= wind_speed <= 7.9):
    W = 4
elif (8.0 <= wind_speed <= 10.7):
    W = 5
elif (10.8 <= wind_speed <= 13.8):
    W = 6
elif (13.9 <= wind_speed <= 17.1):
    W = 7
elif (17.2 <= wind_speed <= 20.7):
    W = 8
elif (20.8 <= wind_speed <= 24.4):
    W = 9
elif (24.5 <= wind_speed <= 28.4):
    W = 10
elif (28.5 <= wind_speed <= 32.6):
    W = 11
else:
    W = 12

# 風向
if W == 0:
    Dir = "C"
elif (Deg < 11.25) or (Deg >= 348.75):
    Dir = "N"
elif (11.25 <= Deg < 33.75):
    Dir = "NNE"
elif (33.75 <= Deg < 56.25):
    Dir = "NE"
elif (56.25 <= Deg < 78.75):
    Dir = "ENE"
elif (78.75 <= Deg < 101.25):
    Dir = "E"
elif (101.25 <= Deg < 123.75):
    Dir = "ESE"
elif (123.75 <= Deg < 146.25):
    Dir = "SE"
elif (146.25 <= Deg < 168.75):
    Dir = "SSE"
elif (168.75 <= Deg < 191.25):
    Dir = "S"
elif (191.25 <= Deg < 213.75):
    Dir = "SSW"
elif (213.75 <= Deg < 236.25):
    Dir = "SW"
elif (236.25 <= Deg < 258.75):
    Dir = "WSW"
elif (258.75 <= Deg < 281.25):
    Dir = "W"
elif (281.25 <= Deg < 303.75):
    Dir = "WNW"
elif (303.75 <= Deg < 326.25):
    Dir = "NW"
elif (326.25 <= Deg < 348.75):
    Dir = "NNW"

print(Dir, W)
