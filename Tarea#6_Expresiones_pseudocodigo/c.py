# Expresiones en pseudocodigo
# Autor: Axel Lopez

# Inicio
# pi, r, resultado
# resultado = (PI*r) ** 2
# Imprimir resultado
# Final

PI = 3.1416
float_r= 0

print("Resolver la siguiente expresión: πr ** 2 ")
float_r = float(input("Ingrese el valor de r: "))

float_R = ((PI * float_r) ** 2)

print("Resultado de la expresión: %1.2f" %(float_R))