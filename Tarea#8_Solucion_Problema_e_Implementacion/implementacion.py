# Solucion implementacion
# Autor: Axel Lopez

float_temperatura = 0
float_R = 0

float_temperatura = float(input("Ingrese la temperatura en grados Celsius: "))

if float_temperatura < -273.15 :
    print("Los grados celsius no puede ser menor a −273,15 °C") 
else :
    float_R = (float_temperatura * 1.8) + 32
    print("La temperatura en grados Fahrenheit es: %1.2f" %(float_R))
