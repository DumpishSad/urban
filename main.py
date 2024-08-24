def sum_all(data):
    sum_elem = 0
    if isinstance(data, (int, float)):
        sum_elem += data
    elif isinstance(data, str):
        sum_elem += len(data)
    elif isinstance(data, dict):
        for key, value in data.items():
            sum_elem += sum_all(key)
            sum_elem += sum_all(value)
    elif isinstance(data, (list, tuple, set)):
        for i in data:
            sum_elem += sum_all(i)
    return sum_elem


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = sum_all(data_structure)
print(result)
