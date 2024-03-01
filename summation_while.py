def summation_while(n):
    total = 0
    current_number = 1
    while current_number <= n:
        total += current_number
        current_number += 1
    return total

a = summation_while(5)

print(a)
