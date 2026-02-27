t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    from collections import Counter
    cnt = Counter(a)
    ans = 0
    for v in cnt.values():
        ans += v // 2
    print(ans)