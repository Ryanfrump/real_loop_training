def list_multiply_while(a: list[int], b: list[int]) -> list[int]:
    new_list = []
    index = 0
    while index < len(a):
        new_list.append(a[index] * b[index])
        index += 1
    return new_list

a = [1,2,3]
b = [4,5,6]

c = list_multiply_while(a,b)
print(c)

