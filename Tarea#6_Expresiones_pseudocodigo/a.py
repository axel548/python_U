# Expresiones en pseudocodigo
# Autor: Axel Lopez

# Inicio
# x, y, z, resultado
# resultado = ((3*y) - (2*x))/(5*z)
# Imprimir resultado
# Final

float_x = 0
float_y = 0
float_z = 0
float_R = 0

print("Resolver la siguiente expresión: (3y - 2z)/5z ")
float_x = float(input("Ingrese el valor de x: "))
float_y = float(input("Ingrese el valor de y: "))
float_z = float(input("Ingrese el valor de z: "))

float_R = ((3*float_y) - (2*float_x)) / (5*float_z)

print("Resultado de la expresión: %1.2f" %(float_R))