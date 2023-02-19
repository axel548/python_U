# Expresiones en pseudocodigo
# Autor: Axel Lopez

# Inicio
# r, a, t, v_0, r_0, resultado
# resultado = ((r*(1/2)*a*(t ** 2)) + (v_0*t) + r_0)
# Imprimir resultado
# Final

float_a = 0
float_r= 0
float_t = 0
float_v_0 = 0
float_r_0 = 0

print("Resolver la siguiente expresión: r1/2at ** 2 + v_0t + r_0")
float_r = float(input("Ingrese el valor de r: "))
float_a = float(input("Ingrese el valor de a: "))
float_t = float(input("Ingrese el valor de t: "))
float_v_0 = float(input("Ingrese el valor de v_0: "))
float_r_0 = float(input("Ingrese el valor de r_0: "))

float_R = ((float_r*(1/2)*float_a*(float_t ** 2)) + (float_v_0*float_t) + float_r_0)

print("Resultado de la expresión: %1.2f" %(float_R))