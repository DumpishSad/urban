def sum_all(data):
    result = 0
    if isinstance(data, (int, float)):
        result += data
    elif isinstance(data, str):
        result += len(data)
    elif isinstance(data, dict):
        for key, value in data.items():
            result += sum_all(key)
            result += sum_all(value)
    elif isinstance(data, (list, tuple, set)):
        for i in data:
            result += sum_all(i)
    return result


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = sum_all(data_structure)
print(result)
