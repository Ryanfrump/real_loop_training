def char_count_foreach(s: str, c: str):
    char_count = 0
    for char in s:
        if c == char:
            char_count += 1
    return char_count


s = "hello"
c = "l"

num_times_c_in_s = char_count_foreach(s,c)
print(num_times_c_in_s)