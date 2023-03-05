
print("---------------------------------------------")
print("Menu")
print("1) Conversión de grados Celsius a Fahrenheit")
print("2) Cálculo del área de un triángulo")
print("---------------------------------------------")
print("\n")
int_opcion = int(input("Ingrese una opción del menu: "))

if int_opcion == 1:
    float_temperatura = 0
    float_R = 0

    print("1) Conversión de grados Celsius a Fahrenheit")
    float_temperatura = float(input("Ingrese la temperatura en grados Celsius: "))

    if float_temperatura < -273.15 :
        print("Los grados celsius no puede ser menor a −273,15 °C") 
    else :
        float_R = (float_temperatura * 1.8) + 32
        print("La temperatura en grados Fahrenheit es: %1.2f" %(float_R))


if int_opcion == 2:
    float_base = 0
    float_altura = 0
    float_R = 0

    print("2) Cálculo del área de un triángulo")
    float_base = float(input("Ingrese la base del triángulo: "))
    float_altura = float(input("Ingrese la altura del triángulo: "))
    
    float_R = (float_base * float_altura) / 2
    print("El área del triángulo es: %1.2f" %(float_R))

    
