int_numero1 = 0
int_numero2 = 0


int_numero1 = int(input("Ingrese el primer valor: "))
int_numero2 = int(input("Ingrese el segundo valor: "))
int_sumaR = int_numero1 + int_numero2
int_restaR = int_numero1 - int_numero2
int_multiplicacionR = int_numero1 * int_numero2
float_divisionR = int_numero1 / int_numero2
int_divisionEnteraR = int_numero1 // int_numero2
float_modulo = int_numero1 % int_numero2


print("Suma: %d" %(int_sumaR))
print("Resta: %d" %(int_restaR))
print("Multiplicación: %d" %(int_multiplicacionR))
print("División: %1.2f" %(float_divisionR))
print("División Entera: %d" %(int_divisionEnteraR))
print("Módulo: %1.2f" %(float_modulo))
# print(" " %())
