mo = set('aeiou')

while True:
    t = input().strip()
    ok = True

    if t == 'end':
        break

    if not any(m in mo for m in t):
        ok = False

    if ok:
        for i in range(len(t) - 1):
            if t[i] == t[i+1] and t[i] not in ('e', 'o'):
                ok = False
                break

    if ok:
        for i in range(len(t) - 2):
            a, b, c = t[i], t[i+1], t[i+2]
            if (a in mo and b in mo and c in mo) or (a not in mo and b not in mo and c not in mo):
                ok = False
                break

    if ok:
        print(f"<{t}> is acceptable.")
    else:
        print(f"<{t}> is not acceptable.")