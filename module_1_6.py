my_dict = {'alex': 182, 'slava': 184, 'karina': 167}
print(my_dict)
print(my_dict['alex'])
print(my_dict.get('sveta'))
my_dict.update({'sveta': 150,
                'danya': 200})
my_dict.pop('alex')
print(my_dict)

my_set = {1, 1, 2, 2, 'bom', True, 'BOM'}
print(my_set)
my_set.update({4, False})
my_set.remove(True)
print(my_set)
