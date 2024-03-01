def char_count_while(s: str, c: str):
    index = 0
    char_count = 0
    while index < len(s):
        if c == s[index]:
            char_count += 1
            index +=1
        elif c != s[index]:
            index += 1
    return char_count
        
s = "hello"
c = "l"

num_times_c_in_s = char_count_while(s,c)
print(num_times_c_in_s)