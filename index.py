nombre = input("Ingrese su nombre completo: ")
edad = int(input("Ingrese su edad: "))
sexo = input("Ingrese su sexo : ")
peso = float(input("Ingrese su peso: "))
altura = float(input("Ingrese su altura: "))

if edad >= 18:
    print("Es mayor de edad")

if sexo == "femenino" and altura > 1.70:
    print("Es una mujer alta")
elif sexo == "masculino" and altura > 1.80:
    print("Es un hombre alto")

if peso / (altura ** 2) <= 15:
    print("Delgadez muy severa")
elif 15 <= peso / (altura ** 2) <= 15.9:
    print("Delgadez severa")
elif 16 <= peso / (altura ** 2) <= 18.4:
    print("Delgadez")
elif 18.5 <= peso / (altura ** 2) <= 24.9:
    print("Peso Saludable")
elif 25 <= peso / (altura ** 2) <= 29.9:
    print("Sobrepeso")
elif 30 <= peso / (altura ** 2) <= 34.9:
    print("Obesidad moderada")
elif 35 <= peso / (altura ** 2) <= 39.9:
    print("Obesidad severa")
else:
    print("Obesidad muy severa (Obesidad morbida)")