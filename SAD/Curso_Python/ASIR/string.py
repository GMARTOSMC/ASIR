my_string = "hola1"

my_other_string = "hola2"

print(my_string)

#Concatenación con espacio en medio

print(my_string + " " + my_other_string)

#Crear salto de línea

variable3 = "Esto es un string\n con salto de línea"

print(variable3)

#Insertar tabulación

variable4 = "\tEsto es un string con tabulación"

print(variable4)

#Escapar carácteres especiales

variable5 = "\\tEsto es un sctring\\ncon salto de línea"

print(variable5)

#Formateo usando format

name, surname, age = "Gonzalo", "Martos", 28

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, age))

# Formateo antiguo

print("Mi nombre es %s %s y mi edad es %d" % (name, surname, age))

#f string

print(f"Mi nombre es {name} {surname} y mi edad es {age}")   

#desenpaquetando carácteres

lenguaje = "python"

a,b,c,d,e,f = lenguaje

# Dividir string (Slice)

language_slice = lenguaje[1:3]

print(language_slice)

#si haces

language_slice = lenguaje[-2]

#coge el segudno carácter al revés

print(language_slice)

language_slice = lenguaje[0:6:2]

#esto coge desde el primero y luego salta de 2 en 2 hasta llega a 6

print(language_slice)

language_slice = lenguaje[1:] #Desde el segundo caracter hasta el final

print(language_slice)

#Invertir el string

language_slice = lenguaje[::-1]

print(language_slice)

###Funciones de string###

#Reemplazar carácteres

fruit = "Strawberry"

print(fruit.replace("r", "R"))

#Convertir el primer carácter del texto en mayúsculas

print(fruit.capitalize())

#Convertir el primer carácter del texto en minúsculas

print(fruit.lower())

#Convertir todo el texto en mayúsculas

print(fruit.upper())

#Contar cuantos caracteres hay que encagen en el fitro que le digamos, por ejemplo que sean r

print(fruit.count("r"))

#Contar cuántos carácteres hay en una palabra

print(len(fruit))

#Ejemplos

print(f"la variable {fruit} tiene: " + str(len(fruit)))

print(fruit.isnumeric())

pocholo = 5

print(pocholo.is_integer())

numero_de_letras = len(fruit)
print(numero_de_letras)
print(str(numero_de_letras).isnumeric())

#verificar si todo el texto está es minúscula

print(fruit.islower())

#Ejemplo Py

print(lenguaje.startswith("py"))