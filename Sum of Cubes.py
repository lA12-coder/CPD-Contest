import sys
import math

it = iter(sys.stdin.read().split())
t = int(next(it))

mx = int((10**12) ** (1/3)) + 2
cubes = [i**3 for i in range(1, mx + 1)]
s = set(cubes)

out = []
for _ in range(t):
    x = int(next(it))
    ok = False
    for c in cubes:
        if c >= x:
            break
        if x - c in s:
            ok = True
            break
    out.append("YES" if ok else "NO")

print("\n".join(out))