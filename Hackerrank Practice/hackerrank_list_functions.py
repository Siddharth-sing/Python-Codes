if __name__ == '__main__':
    n = int(input())
    l = list()
    for i in range(0, n):
        q = input().split()
        if q[0] == "insert":
            l.insert(int(q[2]), int(q[1]))
        elif q[0] == "print":
            print(l)
        elif q[0] == "append":
            l.append(int(q[1]))
        elif q[0] == "sort":
            l.sort()
        elif q[0] == "pop":
            l.pop()
        elif q[0] == "reverse":
            l.reverse()

