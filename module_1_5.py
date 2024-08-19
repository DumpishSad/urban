immutable_var = ([1,3], 'omg', 4)
print(immutable_var)
# immutable_var[0] = 5 // кортеж неизменяемый объект
immutable_var[0][1] = 'var' # а так можно. Бом бом...
print(immutable_var)

mutable_list = [1, 2, 6, 'var', ['bom', 'bom', 2]]
print(mutable_list)
mutable_list[0] = immutable_var
print(mutable_list)
