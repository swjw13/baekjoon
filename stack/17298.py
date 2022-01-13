# 오큰수
# lst에서 pop한 후에 해당 값들을 사용했더니 시간초과가 났고
# pop하는 과정을 제거한 후 index을 통해 답을 전달했더니
# 시간초과가 해결됨
# 결론: pop과정 보다는 indexing을 통한 접근이 시간이 덜 든다
# 결론2: 리스트 초기화 과정에도 신경을 쓰자

import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))

stack = []
ans = [-1 for i in range(N)]
for i in range(N):
    # v = lst.pop(0)

    while len(stack) != 0 and stack[-1][0] < lst[i]:
        low_v, low_i = stack.pop(-1)
        ans[low_i] = lst[i]
    stack.append((lst[i], i))
for i in ans:
    print(i, end=' ')
