import sys


def pyta(lst):
    lst_tmp = lst.copy()
    z = max(lst_tmp)
    lst_tmp.remove(z)
    if z ** 2 == lst_tmp[0] ** 2 + lst_tmp[1] ** 2:
        return True
    else:
        return False


while True:
    l = list(map(int, sys.stdin.readline().split()))
    if l == [0, 0, 0]:
        break
    if pyta(l):
        print("right")
    else:
        print("wrong")
