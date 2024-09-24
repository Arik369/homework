immutable_var = 1,2,"a","b"
print(immutable_var)
#immutable_var = [1] = 3 ошибка, потому что не поддерживается по элементам
#print(immutable_var)
mutable_list = ([1,2,3],1)
print(mutable_list)
mutable_list[0][2] = 2
print(mutable_list)
