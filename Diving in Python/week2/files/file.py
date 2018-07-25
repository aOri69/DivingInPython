# Режимы записи
text_modes = ['r', 'w', 'a', 'r+']
binary_modes = ['br', 'bw', 'ba', 'br+']
f = open('./week2/files/test.txt', text_modes[3])
# Запись
f.write('Writing string to file...')
# Чтение
file_cont = f.read()
print(file_cont)
# Если прочитали раз, то указатель передвинулся в конец файла, и чтение снова ни к чему не приведет
# Поэтому...
f.tell()  # Говорит где указатель
f.seek(0)  # Перемещает указатель на начало
# Закрываем файл
f.close()


# Чтение построчно...
f = open('./week2/files/test.txt', 'r+')
print(f.readline())
f.close()
# Чтение всех строк построчно
f = open('./week2/files/test.txt', 'r+')
print(f.readlines())
f.close()

# """ Правильное открытие файла """
with open('./week2/files/test.txt', 'r') as f:
    print(f.read())
