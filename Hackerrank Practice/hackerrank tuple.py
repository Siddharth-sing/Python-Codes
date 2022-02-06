if __name__ == '__main__':
    n = int(input())
    t = tuple(list(map(int, input().split())))
    print(hash(t))

