def reverse_foreach(s):
    reversed_string = ""
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string


s = "hello"

r = reverse_foreach(s)

print(r)