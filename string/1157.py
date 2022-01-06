a = input()
a = a.upper()

count = [0 for _ in range(26)]
max = 0
for i in a:
    count[ord(i) - ord('A')] += 1
    if count[ord(i) - ord('A')] > max:
        max = count[ord(i) - ord('A')]

tmp = []

for i in range(26):
    if count[i] == max:
        tmp.append(i)
if len(tmp) != 1:
    print("?")
else:
    print(chr(tmp[0] + ord('A')))