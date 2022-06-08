croatic = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

S = input()

for i in croatic:
    S = S.replace(i, 'q')

print(len(S))
