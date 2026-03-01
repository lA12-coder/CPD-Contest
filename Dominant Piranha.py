import sys

it = iter(sys.stdin.read().strip().split())
t = int(next(it))
out = []
for _ in range(t):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    mx = max(a)
    idxs = [i for i in range(n) if a[i] == mx]
    if len(idxs) == n:
        out.append("-1")
        continue
    ans = -1
    for i in idxs:
        if (i > 0 and a[i-1] < a[i]) or (i + 1 < n and a[i+1] < a[i]):
            ans = i + 1
            break
    out.append(str(ans))
print("\n".join(out))