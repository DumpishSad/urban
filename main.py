first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(_str) for _str in first_strings if len(_str) >= 5]
second_result = [(fs, ss) for fs in first_strings for ss in second_strings if len(fs) == len(ss)]
third_result = {i: len(i) for i in first_strings + second_strings if len(i) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)