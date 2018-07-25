import random

collections = ['list', 'tuple']  # Список
collections.append('OrderedDict')  # Добавляем
collections.extend(['ponyset', 'unicorndict'])  # Расширяем
collections += [None]  # Добавляем
del collections[4]  # Удаляем
for idx, collection in enumerate(collections):
    print('#{} {}'.format(idx, collection))


tag_list = ['python', 'course']
print(', '.join(tag_list))

numbers = []
for _ in range(40):
    numbers.append(random.randint(1, 99))
print(sorted(numbers, reverse=True))
print(numbers)
