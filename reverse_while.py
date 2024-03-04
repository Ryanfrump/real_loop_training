def reverse_while(s):
    reversed_string = ""
    index = len(s) - 1
    while index >= 0:
        reversed_string += s[index]
        index -= 1
    return reversed_string

s = "hello"

r = reverse_while(s)

print(r)