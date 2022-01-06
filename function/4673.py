import heapq


def selfnum(num):
    total = num
    for i in list(str(num)):
        total += int(i)
    return total


a = []

for i in range(10000):
    heapq.heappush(a, selfnum(i))
b = [i for i in range(10000)]

for i in [x for x in b if x not in a]:
    print(i)
