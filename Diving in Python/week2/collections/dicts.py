print('*****************************************************************************')
empty_dict = {}
collections_map = {
    'mutable': ['list', 'set', 'dict'],
    'immutable': ['tuple', 'frozenset']
}
print(collections_map['immutable'])
print(collections_map.get('irresistible', '...Not found'))
print('*****************************************************************************')
beatles_map = {
    'Paul': 'Bass',
    'John': 'Guitar',
    'George': 'Guitar'
}
print(beatles_map)
beatles_map['Ringo'] = 'Drums'
print(beatles_map.setdefault('Alex', 'Vocals'))
print(beatles_map)
print('*****************************************************************************')
print(collections_map)

for key in collections_map:
    print(key)

for key in collections_map.keys():
    print(key)

for value in collections_map.values():
    print(value)

for key, value in collections_map.items():
    print('{} - {}'.format(key, value))
print('*****************************************************************************')    
