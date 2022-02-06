# To convert list into string we use join.

def mutation(string, position, character):
    lst = list(map(str, [i for i in string]))
    lst[position] = character
    string = "".join(lst)
    return string


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutation(s, int(i), c)
    print(s_new)
