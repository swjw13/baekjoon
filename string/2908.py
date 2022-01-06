a, b = list(map(int, input().split()))

lst_a = list(str(a))
lst_a.reverse()
lst_b = list(str(b))
lst_b.reverse()

A = int("".join(lst_a))
B = int("".join(lst_b))

print(max(A, B))