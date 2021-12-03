import os
import colorama

colorama.init()
white = "\x1b[1;37;40m" 
red = "\x1b[1;31;222m"

def limpiar():
    if os.name =="nt":
        os.system("cls")
    else:
        os.system("clear")
        
def convertir(valor): #función para verificar y convertir un número ingresado por teclado
    while valor == "" or valor.isdecimal() == False:
            limpiar()
            print(f"{white}Error")
            print(f"{white}Ingrese nuevamente:")
            valor = input(f">>>{red} ")
    valor = int(valor)
    return valor
def area(a,b):
    c = a*b
    return c
limpiar()
print(f'{white}Ejercicio 5: Area de un Rectangulo')

num1 = input(f'{white}Ingrese la base: ')
num1 = convertir(num1)
num2 = input(f'{white}Ingrese la altura: ')
num2 = convertir(num2)
limpiar()
area_rectangulo = area(num1,num2)
print(f'{white}El area del rectangulo es: {red} {area_rectangulo}')
input(f'{white}Presione una tecla cualquiera para terminar...')