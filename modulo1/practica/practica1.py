#                 Ejercicios Nro 1
# Instrucciones : 
#  crear un repositorio en github  (de forma publica , revisar video parte inicial de la grabacion)
#  realizar un archivo por problema 
#  trabajarlo en local y subir los archivos o trabajarlo por codespace
# 1. Realizar un programa que pida tus datos personales para ingresar por teclado(inputs)
#  e imprimirlos. 
a=input("ingresa tus nombres: ")
b=input("ingresa tus apellidos: ")
c=in(input("ingresa tu edad: "))
# 2. Ingrese un valor por teclado e imprima el tipo de dato
a=input("ingrese un leta: ")
b: type(a)
print(c)
# 3. Realice un programa que calcule la suma de los numeros hasta el valor ingresado.
# Ejemplo : Si ingresa 5 se tendra que calcular 1+2+3+4+5
Number= int(input("ingrese la cantidad de numeros a sumar "))
suma=0
for i in range (1, numero + 1):
    suma += i
print("la suma de los numeros hasta", numero, "es: ", suma)

# 4.Realizar un programa que permita saber si un usario puede obtener un tarjeta de credito
# condiciones : ser mayor de 18 años , un ingreso mensual de 1000 soles mensual.
# si cumple con las 2 condiciones imprimir que tipo de tarjeta puede obtener
# si su ingreso mensual es de 1000 hasta 3000 soles es tarjeta de clasica , mayor a ello tarjeta dorada.
Edad=int(input("ingrese su edad: "))
if edad>= 18:
    ingreso=float(input("Digite su ingreso mensual, soles: "))
    if  ingreso>=1000:
        print("Feliciades!, puede obtener una tarjeta de credito")
        if ingreso<=3000:
            print("Con este ingreso aplica a una tarjeta de credito clasica")
        else: 
            print("su ingreso mensual es suficiente para una tarjeta dorada")
    else: 
        print("su ingeso mensual es insuficiente")    
else:
    print:("No cumple con la edad minima, debe tener 18")