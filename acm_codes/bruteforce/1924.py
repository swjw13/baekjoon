# https://www.acmicpc.net/problem/1924
# 2007년

x, y = list(map(int, input().split()))
month_date = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
weekday = {1: "MON", 2: "TUE", 3: "WED", 4: "THU", 5: "FRI", 6: "SAT", 0: "SUN"}
cnt = y
for i in range(1, x):
    cnt += month_date[i]

print(weekday[cnt % 7])