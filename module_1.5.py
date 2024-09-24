immutable_var = 1,2,"a","b"
print(immutable_var)
#immutable_var = [1] = 3 ошибка, потому что кортежи не поддерживают изменения по элементам
#print(immutable_var)
mutable_list = [1,2,3,'a','b']
print(mutable_list)
mutable_list.extend(['ya zaeb..... postoyanno  menyat'])
print(mutable_list)