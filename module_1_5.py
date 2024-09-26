immutable_var = 1, "Данил", 2.0, True
print(immutable_var)
# immutable_var [0] = 2 Данную операцию выполнить невозможно, т.к. элементы в кортеже являются неизменяемыми
mutable_list = [2, "Наташа", 3.0, False]
print(mutable_list)
mutable_list[0] = 'Привет'
mutable_list[1] = 3
mutable_list[2] = True
mutable_list[3] = 3.0
print(mutable_list)