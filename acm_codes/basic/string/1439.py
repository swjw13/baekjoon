# https://www.acmicpc.net/problem/1439
# 뒤집기
import re
S = input()

zeros = re.findall(r"0+", S)
ones = re.findall(r"1+", S)
print(min(len(zeros), len(ones)))