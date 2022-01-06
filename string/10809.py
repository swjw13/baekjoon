a = dict()
for i in range(26):
    a[i] = -1

S = input()
for i in range(len(S)):
    idx = ord(S[i]) - ord('a')
    if a[idx] == -1:
        a[idx] = i

for i in a.values():
    print(i)