# Desarrollar un programa que imprima el cuadrado del n´umero que el
# usuario ingresa mientras que el n´umero ingresado no sea negativo.

while True:
    numero = int(input("Ingresa un número: "))
    if numero < 0:
        break
    cuadrado = numero ** 2
    print(f"El cuadrado de {numero} es: {cuadrado}")
