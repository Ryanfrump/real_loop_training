def char_count_for(s: str, c: str) -> str:
    char_count = 0
    for i in range(len(s)):
        if c == s[i]:
            char_count += 1
    return char_count

s = "hello"
c = "l"

num_times_c_in_s = char_count_for(s,c)
print(num_times_c_in_s)