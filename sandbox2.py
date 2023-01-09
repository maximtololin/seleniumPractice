

# time_mins – количество минут, которое провел на сайте
#
# start_hours – время в часах, когда человек зашел на сайт
#
# start_mins – время в минутах, когда человек зашел на сайт

# Sample Input 1:
#
# 120
# 19
# 0
# Sample Output 1:
#
# 21 0

time_mins = int(input())
time_hours = int(input())
start_mins = int(input())

a = time_mins // 60
b = time_mins % 60

c = time_hours + a
d = start_mins + b


print(c, d)
