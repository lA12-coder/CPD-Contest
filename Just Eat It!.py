import sys

it = iter(sys.stdin.read().split())
t = int(next(it))
out = []

for _ in range(t):
    n = int(next(it))
    a = [int(next(it)) for _ in range(n)]
    total = sum(a)

    cur = 0
    mx_pref = -10**30
    for i in range(n - 1):
        cur += a[i]
        if cur > mx_pref:
            mx_pref = cur

    cur = 0
    mx_suf = -10**30
    for i in range(n - 1, 0, -1):
        cur += a[i]
        if cur > mx_suf:
            mx_suf = cur

    best = max(mx_pref, mx_suf)
    out.append("YES" if total > best else "NO")

print("\n".join(out))