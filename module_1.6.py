my_dict = {'Artur':1983, 'Rita':2005, 'Veronika':2010}
print(my_dict)
print(my_dict['Artur'])
my_dict ['Alexsei'] = 2000
print(my_dict['Alexsei'])
my_dict.update({'Sasha':1989,
                'Masha':1990})
print(my_dict)
f = my_dict.pop('Sasha')
print(my_dict)
print(f)
print(my_dict)
# множество
my_set = {2002, 2003, 2004, 2002,'Artur',(5,6,7)}
print(my_set)
list=[2002,2003,2004,2002,'Artur',(5,6,7)]
list=set(list)
print(list.add(13))
print(list.add(15))
print(list)
print(list.discard(2004))
print(list)