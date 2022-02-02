if __name__ == '__main__':
    n = int(input())
    rec = list()
    fLst = list()

    for i in range(0, n):
        rec.append([input(), float(input())])

    s = set()

    for i in range(0, n):
        s.add(rec[i][1])

    lowLst = sorted(s)
    secLow = lowLst[1]

    for i in range(0, n):
        if rec[i][1] == secLow:
            fLst.append(rec[i][0])

    for i in sorted(fLst):
        print(i)
