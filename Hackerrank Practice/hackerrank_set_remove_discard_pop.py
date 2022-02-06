if __name__ == '__main__':
    n = int(input())
    s = set(list(map(int, input().split())))
    o = int(input())
    for i in range(0, o):
        q = input().split()
        if q[0] == 'remove':
            s.remove(int(q[1]))
        elif q[0] == 'discard':
            s.discard(int(q[1]))
        else:
            s.pop()
    print(sum(s))


