X, Y = map(int, input().split())

a_1 = X
a_2= Y
a_i = 0

for i in range(3, 11):
    a_str = str(a_1 + a_2)
    a_i = int(a_str[::-1])
    a_1, a_2 = a_2, a_i

print(a_i)
