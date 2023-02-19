# Expresiones en código
# Autor: Axel Lopez

int_a = 5
int_b = 4
int_c = -1
float_R = 0

print("Evaluar las siguientes expresiones con los siguientes valores: ")
print("A: %d, B: %d, C: %d" %(int_a, int_b, int_c))


# 1
float_R = (((int_b*int_a) - (int_b ** 2))/(4*int_c))
print("1) B * A – B ** 2 / 4 * C , Resultado: %1.2f" %(float_R))


# 2
float_R = (int_a*int_b) / (2 ** 3)
print("2) (A * B) / 2 ** 3 , Resultado: %1.2f" %(float_R))


# 3
float_R = (((int_b + int_c) / (2 * int_a + 15)) * 2 * int_b) -4
print("3) (((B + C) / 2 * A + 15) * 2 * B) – 4 , Resultado: %1.2f" %(float_R))


# 4
float_R = (3 * (int_a ** 4)) - (5 * (int_b ** 3)) + int_c -12
print("4) 3 * A ** 4 – 5 * B ** 3 + C -12 , Resultado: %1.2f" %(float_R))


# 5
float_R = 3 + 2 * (18 - (4 ** 2)) - 32
print("5) 3 + 2 * (18 – 4 ** 2) – 32, Resultado: %1.2f" %(float_R))