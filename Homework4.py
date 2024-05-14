immutable_var = 1, 2, 3, 4, "a", "b"
print(immutable_var)
#Кортеж относят к неизменяемым типам данных, однако внутри он может содержать изменяемые типы, например списки
#Пример: Попытка изменить один из элементоа кортежа: immutable_var[0] = 228 print(immutable_var), то выдаст ошибку
mutable_list = ["яблоки", "груши", "арбуз", "зубная паста"]
print(mutable_list)
mutable_list.extend([2, "палки колбасы"])
print(mutable_list)
mutable_list.append("грецкий орех")
print(mutable_list)
mutable_list.remove("яблоки")
print(mutable_list)
