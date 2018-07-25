odd_set = set()
even_set = set()

for i in range(10):
    if i % 2:
        odd_set.add(i)
    else:
        even_set.add(i)
print(odd_set)
print(even_set)
union_set = odd_set | even_set
# Аналогично пересечения и разность & и -
union_set.remove(2)
print(union_set)
