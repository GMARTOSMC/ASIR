### Loops ###

# While

# Forma típica con el else dándole una salida

#My_condition = 0

#while My_condition < 10:
  #  print(My_condition)
 #   My_condition +=2
#else:
 #   print("Mi condición es mayor o igual a 10")


#Tabla del 8

print("Tabla de multiplicar")

Tabla = input("Dime un número del 1 al 10 para hacer su tabla\n")
Multiplicador = 0

while Multiplicador < 10:
    Multiplicador += 1
    Resultado = (int(Tabla) * int(Multiplicador))
    print(str(Tabla)  + "*" + str(Multiplicador) + "=" + str(Resultado))

else:
    print("Se detiene la ejecución")
print("Fin de programa")
