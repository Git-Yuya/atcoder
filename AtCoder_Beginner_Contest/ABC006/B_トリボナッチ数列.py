n = int(input())

a_1 = 0
a_2 = 0
a_3 = 1

if n == 1:
    a_n = a_1
elif n == 2:
    a_n = a_2
elif n == 3:
    a_n = a_3

for i in range(3, n):
    a_n = (a_1 + a_2 + a_3) % 10007
    a_1, a_2, a_3 = a_2, a_3, a_n

print(a_n)
