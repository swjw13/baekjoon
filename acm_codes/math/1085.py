x, y, w, h = list(map(int, input().split()))

x_min = min(x, w - x)
y_min = min(y, h - y)

total_min = min(x_min, y_min)

print(total_min)
