# Problema 1
"""Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma 
automática el precio que debe cobrar a sus clientes por entrar.

- El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada.

- Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar 5 monedas y si es mayor de 18 años, 10 monedas."""

# Pedir la edad del cliente
edad = int(input("Por favor, ingresa tu edad: "))

# Calcular el precio de la entrada según la edad
if edad < 4:
    precio_entrada = 0
elif 4 <= edad <= 18:
    precio_entrada = 5
else:
    precio_entrada = 10

# Mostrar el precio de la entrada al usuario
print("El precio de la entrada es:", precio_entrada, "monedas.")

# Problema 2
"""Escribir un programa que pida al usuario un número entero y retorne un triángulo rectángulo como el 
ejemplo de abajo, de altura que sea el número introducido. Imprimir la cadena retornada por la función.
*
**
***
****"""

# Pedir al usuario un número entero
altura = int(input("Por favor, ingresa un número entero para la altura del triángulo: "))

# Función para generar un triángulo rectángulo
def generar_triangulo_rectangulo(altura):
    resultado = ""
    for i in range(1, altura + 1):
        resultado += "*" * i + "\n"
    return resultado

# Llamar a la función y mostrar el triángulo rectángulo
triangulo = generar_triangulo_rectangulo(altura)
print(triangulo)