def list_multiply_for(a: list[int], b: list[int]):
    new_list = []
    for i in range(len(a)):
        new_list.append(a[i] * b[i])
    return new_list

a = [1,2,3]
b = [4,5,6]

c = list_multiply_for(a,b)
print(c)