# Ejercicio Practica 1
# Autor: Axel Lopez

int_dias_entrada= 0
int_anios = 0
int_meses = 0
int_dias = 0


int_dias_entrada = int(input("Ingrese los días: "))


int_anios = int(int_dias_entrada/365)
int_anios_res = int_dias_entrada%365
int_meses = int(int_anios_res/30)
int_dias = int_anios_res%30


print("Los días %d, equivalen a:" %(int_dias_entrada))
print(" %d Años" %(int_anios))
print(" %d Meses" %(int_meses))
print(" %d Días" %(int_dias))