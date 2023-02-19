# Expresiones en pseudocodigo
# Autor: Axel Lopez

# Inicio
# n, x, resultado
# resultado = (n*(n-1)*(x ** 2))/2
# Imprimir resultado
# Final

float_n = 0
float_x= 0


print("Resolver la siguiente expresión: (n(n-1)x**2) / 2")
float_n = float(input("Ingrese el valor de n: "))
float_x = float(input("Ingrese el valor de x: "))


float_R = (float_n*(float_n-1)*(float_x ** 2))/2

print("Resultado de la expresión: %1.2f" %(float_R))