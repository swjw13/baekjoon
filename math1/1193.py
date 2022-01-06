X = int(input())

tmp = 0
i = 1
while True:
    tmp += i
    if tmp >= X:
        break
    i += 1

# 이 때 나온 i값이 그 대각선의 정보를 담고 있을 것임
# i 가 홀수: 1열부터 시작

tmp = tmp - X

if i % 2 == 0:
    print("{}/{}".format(i - tmp, 1 + tmp))
else:
    print("{}/{}".format(1 + tmp, i - tmp))
