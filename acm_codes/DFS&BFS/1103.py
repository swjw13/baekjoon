import sys
from collections import deque

dxdy = [(-1, 0), (1, 0), (0, 1), (0, -1)]
input = sys.stdin.readline

N, M = list(map(int, input().split()))
board = []
for _ in range(N):
    board.append(list(input().strip()))

ans = -1
loop = False
q=deque([(0,0,0,{(0,0)})])
while q:
    r,c,t,v=q.popleft()
    ans=max(ans,t)
    num=int(board[r][c])
    for dx,dy in dxdy:
        nr=r+dx*num
        nc=c+dy*num
        if (nr,nc) in v:
            loop=True
            break
        else:
            if 0<=nr<N and 0<=nc<M and board[nr][nc]!="H":
                new_v = v.union({(nr,nc)})
                q.append((nr,nc,t+1,new_v))
    if loop:
        break

if loop:
    print(-1)
else:
    print(ans + 1)
