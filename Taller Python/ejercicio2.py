#  Imprimir un listado con los n´umeros impares desde 1 hasta 999 y
#  seguidamente otro listado con los n´umeros pares desde 2 hasta 1000 

# Listado de números impares
print("Números impares:")
for num in range(1, 1000, 2):
    print(num)

# Listado de números pares
print("Números pares:")
for num in range(2, 1001, 2):
    print(num)
