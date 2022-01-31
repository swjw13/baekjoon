x1, y1 = list(map(int, input().split()))
x2, y2 = list(map(int, input().split()))
x3, y3 = list(map(int, input().split()))

x_fin, y_fin = None, None
if x1 == x2:
    x_fin = x3
elif x1 == x3:
    x_fin = x2
else:
    x_fin = x1

if y1 == y2:
    y_fin = y3
elif y1 == y3:
    y_fin = y2
else:
    y_fin = y1

print(x_fin, y_fin)
