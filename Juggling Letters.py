t = int(input())
for _ in range(t):
    n = int(input())
    cnt = [0] * 26
    for _ in range(n):
        s = input().strip()
        for c in s:
            cnt[ord(c) - 97] += 1
    ok = True
    for v in cnt:
        if v % n != 0:
            ok = False
            break
    print("YES" if ok else "NO")