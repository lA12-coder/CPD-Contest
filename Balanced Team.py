import sys

it = iter(sys.stdin.read().split())
n = int(next(it))
a = [int(next(it)) for _ in range(n)]
a.sort()

l = 0
ans = 1
for r in range(n):
    while a[r] - a[l] > 5:
        l += 1
    ans = max(ans, r - l + 1)

print(ans)