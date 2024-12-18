my_list = [2,4,5,6,7,8]

for number in my_list:
    print(number)

my_tupla = (1,2,3)

for item in my_tupla:
    print(item)

my_set = {"8x1=8",45,56,78}

print(my_set)

my_dict = {"Nombre": "Pepe", 34: "Hola"}

x = my_dict.keys()

for item in my_dict:
    print(my_dict[item])

print(type(my_tupla))

print(my_dict[34])

for item in my_dict:
    if item == "Nombre":
        print("Encontrado la clave en el diccionario")