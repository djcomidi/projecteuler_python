reversibles = 0
for t in [2, 3, 4, 6, 7, 8]:
    for n in range(10 ** (t - 1), 10 ** t):
        if n % 10 == 0:
            continue
        revn = int(str(n)[::-1])
        if revn < n:
            continue
        if set(str(n + revn)) <= set("13579"):
            reversibles += 2
    message = "10**%d -> %d" % (t, reversibles)
    print(message)
print(reversibles)
