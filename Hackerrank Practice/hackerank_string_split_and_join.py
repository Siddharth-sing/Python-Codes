# In Python, a string can be split on a delimiter.
#
# Example:
#
# >>> a = "this is a string"
# >>> a = a.split(" ") # a is converted to a list of strings.
# >>> print a
# ['this', 'is', 'a', 'string']
# Joining a string is simple:
#
# >>> a = "-".join(a)
# >>> print a
# this-is-a-string

if __name__ == '__main__':
    s = input()
    s = s.split(" ")
    print(s)
    s = " ".join(s)
    print(s)
