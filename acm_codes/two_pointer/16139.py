# https://www.acmicpc.net/problem/16139
# 인간-컴퓨터 상호작용
from collections import defaultdict
import sys

word = str(sys.stdin.readline())
length = len(word)
dic = []
tmp = defaultdict(int)
tmp[word[0]] += 1
dic.append(tmp)
for i in range(1, length):
    tmp = defaultdict(int)
    tmp.update(dic[i - 1])
    tmp[word[i]] += 1
    dic.append(tmp)

T = int(sys.stdin.readline())
for _ in range(T):
    w, start, end = sys.stdin.readline().split()
    end = int(end)
    start = int(start)
    if start == 0:
        sys.stdout.write("{}\n".format(dic[end][w]))
    else:
        sys.stdout.write("{}\n".format(dic[end][w] - dic[start - 1][w]))
