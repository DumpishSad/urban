def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print('----------------------1')
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [7, "it's my", [1, 2, 3]]
values_dict = {'a': 'wasd', 'b': 1, 'c': 3}

print('----------------------2')
print_params(*values_list)
print_params(**values_dict)

print('----------------------3')
values_list_2 = [699, ':(']
print_params(*values_list_2, 42)