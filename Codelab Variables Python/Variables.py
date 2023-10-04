"""Define una variable de cada tipo de primitivo"""

# Entero
edad = 32
# Flotante
estatura = 1,68
# Booleano
trabajador = True
# Cadena
nombre = "edgar"

#i. Concatena a la cadena las otras variables aplicando la conversión correcta para funcionar, guarda el resultado en una variable

concatena = "Hola mi nombre es " + str(nombre) + " y tengo " + str(edad) + " años " + " mi estatura es " + str(estatura) + " y soy muy trabajador " + str(trabajador)

#ii. Investiga sobre el límite de los enteros y los flotantes en python y anotar sus descubrimientos como comentarios en el archivo"""

# Los enteros en Python son de precisión arbitraria, por lo que no tienen un límite superior práctico.
# Los flotantes siguen el estándar IEEE 754 y tienen límites de representación, pero son muy grandes.


# iii. Aplica la fórmula de la suma de los primeros n números pares (investigar), tomando como n la variable de tipo entero y almacenar el resultado en una variable"""
n = 40
resultado = 0
for i in range (2, n + 1, 2):
  resultado += i
print ("La suma de los primeros n números pares es", resultado)

#iv. Imprimir los resultados de las tareas anteriores
print(concatena)
print("edad:",edad)
print("estatura:",estatura)
print("trabajador:",trabajador)
print("nombre:",nombre)