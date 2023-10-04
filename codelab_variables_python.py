"""Define una variable de cada tipo de primitivo"""

# Entero
edad = 32
# Flotante
estatura = 1,68
# Booleano
boolean = True
# Cadena
nombre = "edgar"

#i. Concatena a la cadena las otras variables aplicando la conversión correcta para funcionar, guarda el resultado en una variable

concatena = "Hola mi nombre es " + str(nombre) + " y tengo " + str(edad) + " años " + " mi estatura es " + str(estatura) + " y soy muy trabajador " + str(boolean)

#ii. Investiga sobre el límite de los enteros y los flotantes en python y anotar sus descubrimientos como comentarios en el archivo"""

# Los enteros en Python son de precisión arbitraria, por lo que no tienen un límite superior práctico.
# Si por ejemplo se usan enteros de 32 bits el rango a representar es de -2^31 a 2^31–1, es decir, -2.147.483.648 a 2.147.483.647. 
# Con 64 bits, el rango es de -9.223.372.036.854.775.808 hasta 9.223.372.036.854.775.807.

# Los float a diferencia de los int tienen unos valores mínimo y máximos que pueden representar. 
# La mínima precisión es 2.2250738585072014e-308 y la máxima 1.7976931348623157e+308.


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
print("boolean:",boolean)
print("nombre:",nombre)