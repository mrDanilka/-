my_dict = {'Danil': 55656566, 'Lena' : 555555}
print(my_dict)
print(my_dict.get('Danil', 'Dasha'))
my_dict.update({'Masha': 5454, 'Max' : 7778})
del my_dict['Danil']
print(my_dict.get('Danil', "Такого ключа нет"))
print(my_dict)
my_set = {69, 69, 69, True, True, 'Danil', 'Danil'}
print(my_set)
my_set.update((5,'Danilka'))
print(my_set)
my_set.discard(5)
print(my_set)
