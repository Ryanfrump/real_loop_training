def reverse_for(s):
    reversed_string = ""
    #len(s)-1 == start next -1 == stop next -1 == step
    for i in range(len(s)-1, -1, -1):
        reversed_string += s[i]
    return reversed_string

s = "hello"

r = reverse_for(s)

print(r)

