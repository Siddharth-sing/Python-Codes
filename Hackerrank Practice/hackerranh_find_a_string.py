def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count


if __name__ == '__main__':
    s = input().strip()
    s_s = input().strip()
    count = count_substring(s, s_s)
    print(count)
