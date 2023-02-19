# Expresiones en pseudocodigo
# Autor: Axel Lopez

# Inicio
# P, r, n, t, resultado
# resultado = P((1 + (r/n))**(n*t))
# Imprimir resultado
# Final

float_P = 0
float_r = 0
float_n = 0
float_t = 0
float_R = 0

print("Resolver la siguiente expresión: P(1 + r/n)**nt ")
float_P = float(input("Ingrese el valor de P: "))
float_r = float(input("Ingrese el valor de r: "))
float_n = float(input("Ingrese el valor de n: "))
float_t = float(input("Ingrese el valor de t: "))


float_R = float_P*((1 + (float_r/float_n)) ** (float_n*float_t))

print("Resultado de la expresión: %1.2f" %(float_R))