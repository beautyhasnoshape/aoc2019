count = 0
for n in range(123257, 647015+1):
    s = str(n)
    a, b, c, d, e, f = int(s[0]), int(s[1]), int(s[2]), int(s[3]), int(s[4]), int(s[5])
    if (a == b or b == c or c == d or d == e or e == f) and (a <= b and b <= c and c <= d and d <= e and e <= f):
        count += 1
    
print(count)

count = 0
for n in range(123257, 647015+1):
    s = str(n)
    a, b, c, d, e, f = int(s[0]), int(s[1]), int(s[2]), int(s[3]), int(s[4]), int(s[5])
    if not(a <= b and b <= c and c <= d and d <= e and e <= f):
        continue

    isOK = False
    l = len(s)
    for i in range(l - 1):
        if i == 0:
            if s[0] == s[1] and s[1] != s[2]:
                isOK = True
                break
            else:
                continue
        elif i == l-2:
            if s[l-1] == s[l-2] and s[l-2] != s[l-3]:
                isOK = True
                break
            else:
                continue
        if s[i] != s[i-1] and s[i] == s[i+1] and s[i+1] != s[i+2]:
            isOK = True
            break
    if isOK:
        count += 1

    # or using a hardcoded, but shorter form:
    # if a == b and b != c or a != b and b == c and c != d or b != c and c == d and d != e or c != d and d == e and e != f or d != e and e == f:
    #     count += 1

print(count)