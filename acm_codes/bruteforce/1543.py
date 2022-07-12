# https://www.acmicpc.net/problem/1543
# 문서 검색

import re

big = input()
small = input()

cnt = 0
for i in re.finditer(small, big):
    cnt += 1
print(cnt)