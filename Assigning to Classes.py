import sys

it = iter(sys.stdin.read().split())
t = int(next(it))
res = []
for _ in range(t):
    n = int(next(it))
    a = [int(next(it)) for _ in range(2*n)]
    a.sort()
    best = 10**30
    for i in range(n):
        best = min(best, a[i+n] - a[i])
    res.append(str(best))
print("\n".join(res))